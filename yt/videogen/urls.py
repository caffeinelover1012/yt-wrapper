from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate/', views.generate_video, name='generate_video'),
    path('myvideos/', views.user_videos, name='user_videos'),
    path('video/<int:video_id>/', views.video_details, name='video_details'),
]
