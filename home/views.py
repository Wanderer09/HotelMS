from django.shortcuts import render,redirect
from .models import Contact,Restaurant_Booking
from room.models import Room,Room_type,services
def index(request):
    count=Room_type.objects.all().count()
    if (count == 0):
        Room_type.objects.create(room_type='Single',room_price='2000',smoking_status=True,room_rating=5,room_description=" A room assigned to one person. May have one or more beds.",number_of_guests=1,show_on_homepage=True,room_img='/img/bed-2.jpg')
        Room_type.objects.create(room_type='Double',room_price='3000',smoking_status=True,room_rating=4,room_description="A room assigned to two people. May have one or more beds.",number_of_guests=2,show_on_homepage=True,room_img='/img/bed-3.jpg')
        Room_type.objects.create(room_type='Triple',room_price='4000',smoking_status=True,room_rating=4,room_description=" A room assigned to three people. May have two or more beds.",number_of_guests=3,show_on_homepage=True,room_img='/img/bed-4.jpg')
        Room_type.objects.create(room_type='Quad',room_price='5000',smoking_status=True,room_rating=4,room_description="A room assigned to four people. May have two or more beds.",number_of_guests=4,show_on_homepage=True,room_img='/img/bed-5.jpg')
        Room_type.objects.create(room_type='Queen',room_price='3500',smoking_status=True,room_rating=5,room_description=" A room with a queen-sized bed. May be occupied by one or more people.",number_of_guests=6,show_on_homepage=True,room_img='/img/bed-6.jpg')
        Room_type.objects.create(room_type='King',room_price='4500',smoking_status=True,room_rating=3,room_description="A room with a king-sized bed. May be occupied by one or more people.",number_of_guests=7,show_on_homepage=True,room_img='/img/bed-1.jpg')
        Room_type.objects.create(room_type='Twin',room_price='4000',smoking_status=True,room_rating=2,room_description=" A room with two beds. May be occupied by one or more people.",number_of_guests=5,show_on_homepage=False,room_img='/img/bed-2.jpg')
        Room_type.objects.create(room_type='Double-double',room_price='6000',smoking_status=True,room_rating=3,room_description="A room with two double (or perhaps queen) beds. May be occupied by one or more people.",number_of_guests=7,show_on_homepage=False,room_img='/img/bed-4.jpg')
    count_of_rooms=Room.objects.all().count()
    if (count_of_rooms==0):
        Room.objects.create(room_number=101,room_type_id=4,room_status='available',room_floor=1)
        Room.objects.create(room_number=102,room_type_id=3,room_status='available',room_floor=1)
        Room.objects.create(room_number=103,room_type_id=2,room_status='booked',room_floor=1)
        Room.objects.create(room_number=104,room_type_id=1,room_status='available',room_floor=1)
        Room.objects.create(room_number=105,room_type_id=5,room_status='available',room_floor=1)
        Room.objects.create(room_number=106,room_type_id=7,room_status='available',room_floor=1)
        Room.objects.create(room_number=107,room_type_id=4,room_status='available',room_floor=1)
        Room.objects.create(room_number=108,room_type_id=4,room_status='available',room_floor=1)
        Room.objects.create(room_number=109,room_type_id=6,room_status='occupied',room_floor=1)
        Room.objects.create(room_number=110,room_type_id=6,room_status='available',room_floor=1)
        Room.objects.create(room_number=201,room_type_id=1,room_status='available',room_floor=2)
        Room.objects.create(room_number=202,room_type_id=2,room_status='available',room_floor=2)
        Room.objects.create(room_number=203,room_type_id=3,room_status='booked',room_floor=2)
        Room.objects.create(room_number=204,room_type_id=4,room_status='available',room_floor=2)
        Room.objects.create(room_number=205,room_type_id=4,room_status='available',room_floor=2)
        Room.objects.create(room_number=206,room_type_id=5,room_status='booked',room_floor=2)
        Room.objects.create(room_number=207,room_type_id=5,room_status='available',room_floor=2)
        Room.objects.create(room_number=208,room_type_id=6,room_status='available',room_floor=2)
        Room.objects.create(room_number=209,room_type_id=4,room_status='house_use',room_floor=2)
        Room.objects.create(room_number=210,room_type_id=2,room_status='available',room_floor=2)
        Room.objects.create(room_number=301,room_type_id=1,room_status='available',room_floor=3)
        Room.objects.create(room_number=302,room_type_id=3,room_status='booked',room_floor=3)
        Room.objects.create(room_number=303,room_type_id=5,room_status='available',room_floor=3)
        Room.objects.create(room_number=304,room_type_id=5,room_status='available',room_floor=3)
        Room.objects.create(room_number=305,room_type_id=4,room_status='booked',room_floor=3)
        Room.objects.create(room_number=306,room_type_id=2,room_status='available',room_floor=3)
        Room.objects.create(room_number=307,room_type_id=2,room_status='available',room_floor=3)
        Room.objects.create(room_number=308,room_type_id=3,room_status='booked',room_floor=3)
        Room.objects.create(room_number=309,room_type_id=7,room_status='available',room_floor=3)
        Room.objects.create(room_number=310,room_type_id=6,room_status='available',room_floor=3)
    count_of_services=services.objects.all().count()
    if(count_of_services==0):
        services.objects.create(service_type='Spa & Saloon',service_cost=1500,service_availability=True)
        services.objects.create(service_type='Gym',service_cost=1000,service_availability=True)
        services.objects.create(service_type='private chef',service_cost=1200,service_availability=True)
        services.objects.create(service_type='laundary',service_cost=1600,service_availability=True)
        services.objects.create(service_type='Pick & Drop',service_cost=2000,service_availability=True)
        services.objects.create(service_type='Guided Tour',service_cost=4000,service_availability=False)
        services.objects.create(service_type='Dry Cleaning',service_cost=3000,service_availability=True)
    room_type=Room_type.objects.all()
    room_available_count=[]
    style=[]
    price=[]
    rating=[]
    show_on_homepage=[]
    # images=[]
    if(request.method=='POST'):
        name=request.POST.get('name')
        phonenumber=request.POST.get('phonenumber')
        number_of_persons=request.POST.get('number_of_persons')
        date=request.POST.get('date')
        time=request.POST.get('time')
        Restaurant_Booking.objects.create(name=name,phonenumber=phonenumber,Number_of_persons=number_of_persons,date=date,time=time)
    for i in range(1,count+1):
        a=Room.objects.filter(room_status='available',room_type_id=i).count()
        room_available_count.append(a)
    for i in room_type:
        style.append(i.room_type)
        price.append(i.room_price)
        rating.append(i.room_rating)
        show_on_homepage.append(i.show_on_homepage)
        # images.append(i.room_img)
    mylist=zip(style,price,rating,show_on_homepage,room_available_count)
    data={}
    data["mylist"]=mylist
    data['test']=True
    return render(request,"home/homepage.html",data)

def contact(request):
    thank=False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank=True
        return redirect('Home',permanent=True)
    return render(request, 'home/contact.html',{"thank":thank})

def login(request):
    return render(request,'home/login.html',{})
def about(request):
    return render(request,'home/about.html',{})
