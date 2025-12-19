from django.urls import path
from .views import LeaveListCreate, LeaveApprove

urlpatterns = [
    path('', LeaveListCreate.as_view()),
    path('<int:pk>/action/', LeaveApprove.as_view()),
    
]
