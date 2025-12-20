from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Leave
from .serializers import LeaveSerializer


class EmployeeLeaveView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
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
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
