from rest_framework import serializers
from .models import Expense

# class ExpenseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Expense
#         fields = '__all__'
#         read_only_fields = ['user', 'status']
class ExpenseSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Expense
        fields = [
            "id",
            "username",
            "amount",
            "category",
            "description",
            "status",
            "created_at",
        ]