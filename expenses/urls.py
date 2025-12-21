from django.urls import path
from .views import ExpenseListCreate, ExpenseApprove, ExpenseDelete

urlpatterns = [
    path('', ExpenseListCreate.as_view()),
    path('<int:pk>/', ExpenseDelete.as_view()),          # 👈 DELETE FIX
    path('<int:pk>/action/', ExpenseApprove.as_view()),
]
