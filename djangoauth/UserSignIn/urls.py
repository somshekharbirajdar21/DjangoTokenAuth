from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from . import views


urlpatterns = [
    path("signin/", views.signInView , name="signin"),
    path("login/", ObtainAuthToken.as_view() , name="login")
]
