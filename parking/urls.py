from django.urls import path
from parking.views import *

urlpatterns = [
    path('',home,name='home'),
    path('video_feed/',post_get,name='video_feed')
]