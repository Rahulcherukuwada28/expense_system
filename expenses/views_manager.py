from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Expense
from .serializers import ExpenseSerializer
from users.permissions import IsManager


class ManagerExpenseView(APIView):
    permission_classes = [IsAuthenticated, IsManager]

    def get(self, request):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)


class ManagerExpenseAction(APIView):
    permission_classes = [IsAuthenticated, IsManager]

    def post(self, request, pk):
        try:
            expense = Expense.objects.get(id=pk)
        except Expense.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

        if expense.status != "PENDING":
            return Response({"error": "Already processed"}, status=400)

        action = request.data.get("action")

        if action == "approve":
            expense.status = "APPROVED"
            expense.approved_by = request.user
        elif action == "reject":
            expense.status = "REJECTED"
            expense.approved_by = request.user
        else:
            return Response({"error": "Invalid action"}, status=400)

        expense.save()
        return Response({"status": expense.status})
