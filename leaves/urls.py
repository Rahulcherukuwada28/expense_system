from django.urls import path
from .views import LeaveListCreate, LeaveDelete, LeaveApprove

urlpatterns = [
    path('', LeaveListCreate.as_view()),
    path('<int:pk>/', LeaveDelete.as_view()),
    path('<int:pk>/action/', LeaveApprove.as_view()),  # 👈 THIS FIXES 404
]
