from django.shortcuts import render
from .models import Contact
from room.models import Room,Room_type


def index(request):
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


