from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Expense
from .serializers import ExpenseSerializer
from users.permissions import IsManager


class ExpenseListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Manager sees all expenses
        if request.user.role == "MANAGER":
            expenses = Expense.objects.all().order_by("-id")
        # Employee sees only their expenses
        else:
            expenses = Expense.objects.filter(user=request.user).order_by("-id")

        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Only employees can create expenses
        if request.user.role != "EMPLOYEE":
            return Response(
                {"detail": "Only employees can create expenses"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseApprove(APIView):
    permission_classes = [IsAuthenticated, IsManager]

    def post(self, request, pk):
        try:
            expense = Expense.objects.get(id=pk)
        except Expense.DoesNotExist:
            return Response(
                {"error": "Expense not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if expense.status != "PENDING":
            return Response(
                {"error": "Already processed"},
                status=status.HTTP_400_BAD_REQUEST
            )

        action = request.data.get("action")

        if action == "approve":
            expense.status = "APPROVED"
            expense.approved_by = request.user   # ✅ SAVE MANAGER
        elif action == "reject":
            expense.status = "REJECTED"
            expense.approved_by = request.user   # ✅ SAVE MANAGER
        else:
            return Response(
                {"error": "Invalid action"},
                status=status.HTTP_400_BAD_REQUEST
            )

        expense.save()
        return Response(
            {
                "status": expense.status,
                "approved_by": request.user.username
            },
            status=status.HTTP_200_OK
        )
