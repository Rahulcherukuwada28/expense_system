from django.urls import path
from .views import SignupView, MeView
from .views import ChangePasswordView


urlpatterns = [
    path("signup/", SignupView.as_view()),
    path("me/", MeView.as_view()),
    path("change-password/", ChangePasswordView.as_view()),

    
]
