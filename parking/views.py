import easyocr,json,base64,datetime
from django.utils import timezone
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from .models import *


def login_ceo(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        
        if username == None or password == None:
            context['error_msg'] = "Ma'lumotnilarni to'ldiring"
            return render(request, 'login.html',context)
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)  
            
            if len(user.groups.all().filter(name='Security')) != 0:
                return redirect('home')
            else:
                context['error'] = "Bu tizmga kirishga ruxsat berilmagan"
                return render(request,'login.html',context)
        else:
            context['error']='Login yoki parol xato'
            
    return render(request, 'login.html',context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def home(request): 
    con = {}
    con['parking'] = Parking.objects.filter(author = request.user)
    return render(request, 'home.html',con)

@login_required
def go_parking(request,slug): 
    con = {}
    con['parking'] = Parking.objects.filter(slug=slug).first()
    con['car_parking'] = CarInParking.objects.filter(parking__category__number = con['parking'].category.number).order_by('-started_at')
    con['cars'] = []
    for i in con['car_parking']:   
        hour = timezone.now() - i.started_at.astimezone()
        prices = round(int(hour.seconds) / 3600) * i.price
        if prices == 0:
            prices = i.price
        else:
            prices = prices
        # print(hour.seconds)
        con['cars'].append({
            'car_number':i.car_number,
            'img':i.img,
            'price':i.price,
            'started_at':i.started_at,
            'hour': round(int(hour.seconds) // 3600),
            'prices':prices,
            'status':i.status ,
            'parking':i.parking,
            'slug':i.slug
        })
    return render(request, 'go_parking.html',con)



@csrf_exempt 
def post_get(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        decode_file = base64.b64decode(str(body['image']))
        img_file = open('./car_number/image.jpg', 'wb')
        img_file.write(decode_file)
        img_file.close()
        reader = easyocr.Reader(['en'])
        result = reader.readtext('./car_number/image.jpg', detail = 0)
        parking =  Parking.objects.filter(author=2)[0]
        print(result[0])
        if body['status']:
            create = CarInParking.objects.create(car_number=result[0],parking=parking,img = './car_number/image.jpg')
        else:
            print(0)
            filter_car = CarInParking.objects.filter(car_number = result[0],status = True).update(status=False)
            
    return HttpResponse()
