from django.urls import path
from parking.views import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',login_ceo,name='login'),
    path('logout',logout_user,name='logout_user'),
    path('homw/',home,name='home'),
    path('parking/<slug:slug>/',go_parking,name='go_parking'),
    path('video_feed/',post_get,name='video_feed')
]