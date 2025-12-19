from rest_framework import serializers
from .models import Leave

# class LeaveSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Leave
#         fields = '__all__'
#         read_only_fields = ['user', 'status']
class LeaveSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Leave
        fields = [
            "id",
            "username",
            "start_date",
            "end_date",
            "reason",
            "status",
            "created_at",
        ]