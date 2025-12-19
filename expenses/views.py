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
        if request.user.role == "MANAGER":
            expenses = Expense.objects.all()
        else:
            expenses = Expense.objects.filter(user=request.user)

        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    def post(self, request):
        # 🔒 ROLE CHECK (THIS WAS MISSING)
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

    def post(self, request, pk):   # <-- pk MUST be here
        try:
            expense = Expense.objects.get(id=pk)
        except Expense.DoesNotExist:
            return Response({"error": "Expense not found"}, status=404)

        if expense.status != "PENDING":
            return Response(
                {"error": "Already processed"},
                status=status.HTTP_400_BAD_REQUEST
            )

        action = request.data.get("action")

        if action == "approve":
            expense.status = "APPROVED"
        elif action == "reject":
            expense.status = "REJECTED"
        else:
            return Response(
                {"error": "Invalid action"},
                status=status.HTTP_400_BAD_REQUEST
            )

        expense.save()
        return Response({"status": expense.status})


