from django.urls import path
from .views import uploadphoto, showphoto
urlpatterns = [
    path('upload', uploadphoto, name='upload_photo'),
    path('', showphoto, name="showphoto")
]