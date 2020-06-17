from django.shortcuts import render
from .models import Contact
from room.models import Room,Room_type
def index(request):
    count=Room_type.objects.all().count()
    if (count == 0):
        a=Room_type(room_type='Single',room_price='2000',smoking_status=True,room_rating=5,room_description=" A room assigned to one person. May have one or more beds.",number_of_guests=1)
        b=Room_type(room_type='Double',room_price='3000',smoking_status=True,room_rating=4,room_description="A room assigned to two people. May have one or more beds.",number_of_guests=2)
        c=Room_type(room_type='Triple',room_price='4000',smoking_status=True,room_rating=4,room_description=" A room assigned to three people. May have two or more beds.",number_of_guests=3)
        d=Room_type(room_type='Quad',room_price='5000',smoking_status=True,room_rating=4,room_description="A room assigned to four people. May have two or more beds.",number_of_guests=4)
        e=Room_type(room_type='Queen',room_price='3500',smoking_status=True,room_rating=5,room_description=" A room with a queen-sized bed. May be occupied by one or more people.",number_of_guests=6)
        f=Room_type(room_type='King',room_price='4500',smoking_status=True,room_rating=3,room_description="A room with a king-sized bed. May be occupied by one or more people.",number_of_guests=7)
        g=Room_type(room_type='Twin',room_price='4000',smoking_status=True,room_rating=2,room_description=" A room with two beds. May be occupied by one or more people.",number_of_guests=5)
        h=Room_type(room_type='Double-double',room_price='6000',smoking_status=True,room_rating=3,room_description="A room with two double (or perhaps queen) beds. May be occupied by one or more people.",number_of_guests=7)
        a.save()
        b.save()
        c.save()
        d.save()
        e.save()
        f.save()
        g.save()
        h.save()
    room_type=Room_type.objects.all();
    style=[]
    price=[]
    rating=[]
    for i in room_type:
        style.append(i.room_type)
        price.append(i.room_price)
        rating.append(i.room_rating)
    mylist=zip(style,price,rating)
    data={}
    data["mylist"]=mylist
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


