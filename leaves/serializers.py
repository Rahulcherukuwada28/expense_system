from rest_framework import serializers
from .models import Leave   # means leaves.models.Leave

class LeaveSerializer(serializers.ModelSerializer):
    employee_name = serializers.ReadOnlyField(source='user.username')
    approved_by_name = serializers.ReadOnlyField(source='approved_by.username')

    class Meta:
        model = Leave
        fields = [
            'id',
            'start_date',
            'end_date',
            'reason',
            'status',
            'employee_name',
            'approved_by_name',
            'created_at',
            'approved_by',
        ]
