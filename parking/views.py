from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators import gzip
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np 
import easyocr
import cv2,json,base64
import time
import threading
from PIL import Image
from .models import *


def home(request): 
    conetxt = {}
    conetxt['lists'] = Picture.objects.all().order_by('-id')
    return render(request, 'index.html',conetxt)

@csrf_exempt
def post_get(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        decode_file = base64.b64decode(str(body['image']))
        img_file = open('media/image.jpg', 'wb')
        img_file.write(decode_file)
        img_file.close()
        reader = easyocr.Reader(['en'])
        result = reader.readtext('./media/image.jpg', detail = 0)
        print(result[0])
        create = Picture.objects.create(car_number = result[0]).save()
    return HttpResponse()
