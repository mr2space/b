from django.urls import path
from .views import logUser
urlpatterns = [
    path('', logUser , name="login")
]