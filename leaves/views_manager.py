from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Leave
from .serializers import LeaveSerializer
from users.permissions import IsManager


class ManagerLeaveView(APIView):
    permission_classes = [IsAuthenticated, IsManager]

    def get(self, request):
        leaves = Leave.objects.all()
        serializer = LeaveSerializer(leaves, many=True)
        return Response(serializer.data)


class ManagerLeaveAction(APIView):
    permission_classes = [IsAuthenticated, IsManager]

    def post(self, request, pk):
        try:
            leave = Leave.objects.get(id=pk)
        except Leave.DoesNotExist:
            return Response({"error": "Leave not found"}, status=404)

        if leave.status != "PENDING":
            return Response({"error": "Already processed"}, status=400)

        action = request.data.get("action")

        if action == "approve":
            leave.status = "APPROVED"
            leave.approved_by = request.user
        elif action == "reject":
            leave.status = "REJECTED"
            leave.approved_by = request.user
        else:
            return Response({"error": "Invalid action"}, status=400)

        leave.save()
        return Response({"status": leave.status})
