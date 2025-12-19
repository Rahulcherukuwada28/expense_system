from django.urls import path
from .views import ExpenseListCreate, ExpenseApprove

urlpatterns = [
    path("", ExpenseListCreate.as_view()),
    path("<int:pk>/action/", ExpenseApprove.as_view()),
]
