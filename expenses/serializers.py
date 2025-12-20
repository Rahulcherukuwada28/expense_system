from rest_framework import serializers
from .models import Expense   # means expenses.models.Expense

class ExpenseSerializer(serializers.ModelSerializer):
    employee_name = serializers.ReadOnlyField(source='user.username')
    approved_by_name = serializers.ReadOnlyField(source='approved_by.username')

    class Meta:
        model = Expense
        fields = [
            'id',
            'amount',
            'category',
            'description',
            'status',
            'employee_name',
            'approved_by_name',
            'created_at',
            'approved_by',
        ]
