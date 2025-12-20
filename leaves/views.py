from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Leave
from .serializers import LeaveSerializer
from users.permissions import IsManager


class LeaveListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == "MANAGER":
            leaves = Leave.objects.all()
        else:
            leaves = Leave.objects.filter(user=request.user)

        serializer = LeaveSerializer(leaves, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != "EMPLOYEE":
            return Response(
                {"detail": "Only employees can apply for leave"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LeaveApprove(APIView):
    permission_classes = [IsAuthenticated, IsManager]

    def post(self, request, pk):
        try:
            leave = Leave.objects.get(id=pk)
        except Leave.DoesNotExist:
            return Response({"error": "Leave not found"}, status=404)

        if leave.status != "PENDING":
            return Response(
                {"error": "Already processed"},
                status=status.HTTP_400_BAD_REQUEST
            )

        action = request.data.get("action")

        if action == "approve":
            leave.status = "APPROVED"
            leave.approved_by = request.user
        elif action == "reject":
            leave.status = "REJECTED"
            leave.approved_by = request.user
        else:
            return Response(
                {"error": "Invalid action"},
                status=status.HTTP_400_BAD_REQUEST
            )

        leave.save()
        return Response({"status": leave.status})
