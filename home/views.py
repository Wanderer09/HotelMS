from django.shortcuts import render
from .models import Contact
from room.models import Room,Room_type
def index(request):
    count=Room_type.objects.all().count()
    if (count == 0):
        Room_type.objects.create(room_type='Single',room_price='2000',smoking_status=True,room_rating=5,room_description=" A room assigned to one person. May have one or more beds.",number_of_guests=1,show_on_homepage=True)
        Room_type.objects.create(room_type='Double',room_price='3000',smoking_status=True,room_rating=4,room_description="A room assigned to two people. May have one or more beds.",number_of_guests=2,show_on_homepage=True)
        Room_type.objects.create(room_type='Triple',room_price='4000',smoking_status=True,room_rating=4,room_description=" A room assigned to three people. May have two or more beds.",number_of_guests=3,show_on_homepage=True)
        Room_type.objects.create(room_type='Quad',room_price='5000',smoking_status=True,room_rating=4,room_description="A room assigned to four people. May have two or more beds.",number_of_guests=4,show_on_homepage=True)
        Room_type.objects.create(room_type='Queen',room_price='3500',smoking_status=True,room_rating=5,room_description=" A room with a queen-sized bed. May be occupied by one or more people.",number_of_guests=6,show_on_homepage=True)
        Room_type.objects.create(room_type='King',room_price='4500',smoking_status=True,room_rating=3,room_description="A room with a king-sized bed. May be occupied by one or more people.",number_of_guests=7,show_on_homepage=True)
        Room_type.objects.create(room_type='Twin',room_price='4000',smoking_status=True,room_rating=2,room_description=" A room with two beds. May be occupied by one or more people.",number_of_guests=5,show_on_homepage=False)
        Room_type.objects.create(room_type='Double-double',room_price='6000',smoking_status=True,room_rating=3,room_description="A room with two double (or perhaps queen) beds. May be occupied by one or more people.",number_of_guests=7,show_on_homepage=False)
    count_of_rooms=Room.objects.all().count()
    if (count_of_rooms==0):
        Room.objects.create(room_number=101,room_type_id=4,room_status='a',room_floor=1)
        Room.objects.create(room_number=102,room_type_id=3,room_status='a',room_floor=1)
        Room.objects.create(room_number=103,room_type_id=2,room_status='na',room_floor=1)
        Room.objects.create(room_number=104,room_type_id=1,room_status='a',room_floor=1)
        Room.objects.create(room_number=105,room_type_id=5,room_status='a',room_floor=1)
        Room.objects.create(room_number=106,room_type_id=7,room_status='a',room_floor=1)
        Room.objects.create(room_number=107,room_type_id=4,room_status='a',room_floor=1)
        Room.objects.create(room_number=108,room_type_id=4,room_status='a',room_floor=1)
        Room.objects.create(room_number=109,room_type_id=6,room_status='o',room_floor=1)
        Room.objects.create(room_number=110,room_type_id=6,room_status='a',room_floor=1)
        Room.objects.create(room_number=201,room_type_id=1,room_status='a',room_floor=2)
        Room.objects.create(room_number=202,room_type_id=2,room_status='a',room_floor=2)
        Room.objects.create(room_number=203,room_type_id=3,room_status='na',room_floor=2)
        Room.objects.create(room_number=204,room_type_id=4,room_status='a',room_floor=2)
        Room.objects.create(room_number=205,room_type_id=4,room_status='a',room_floor=2)
        Room.objects.create(room_number=206,room_type_id=5,room_status='na',room_floor=2)
        Room.objects.create(room_number=207,room_type_id=5,room_status='a',room_floor=2)
        Room.objects.create(room_number=208,room_type_id=6,room_status='a',room_floor=2)
        Room.objects.create(room_number=209,room_type_id=4,room_status='m',room_floor=2)
        Room.objects.create(room_number=210,room_type_id=2,room_status='a',room_floor=2)
        Room.objects.create(room_number=301,room_type_id=1,room_status='a',room_floor=3)
        Room.objects.create(room_number=302,room_type_id=3,room_status='na',room_floor=3)
        Room.objects.create(room_number=303,room_type_id=5,room_status='a',room_floor=3)
        Room.objects.create(room_number=304,room_type_id=5,room_status='a',room_floor=3)
        Room.objects.create(room_number=305,room_type_id=4,room_status='na',room_floor=3)
        Room.objects.create(room_number=306,room_type_id=2,room_status='a',room_floor=3)
        Room.objects.create(room_number=307,room_type_id=2,room_status='a',room_floor=3)
        Room.objects.create(room_number=308,room_type_id=3,room_status='na',room_floor=3)
        Room.objects.create(room_number=309,room_type_id=7,room_status='a',room_floor=3)
        Room.objects.create(room_number=310,room_type_id=6,room_status='a',room_floor=3)
    room_type=Room_type.objects.all()
    room_available_count=[]
    style=[]
    price=[]
    rating=[]
    show_on_homepage=[]
    for i in range(1,count+1):
        a=Room.objects.filter(room_status='a',room_type_id=i).count()
        room_available_count.append(a)
    for i in room_type:
        style.append(i.room_type)
        price.append(i.room_price)
        rating.append(i.room_rating)
        show_on_homepage.append(i.show_on_homepage)
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
    return render(request, 'home/contact.html',{"thank":thank})

def login(request):
    return render(request,'home/login.html',{})
