from django.shortcuts import render
from bookings.models import booking_guest_details

# Create your views here.
def reception_home(request):
	return render(request,'reception/reception_home.html')
def guest_list(request):
	list=booking_guest_details.objects.all()
	name=[]
	country=[]
	town=[]
	mail=[]
	phone=[]
	in_date=[]
	out_date=[]
	room_count=[]
	guest_count=[]
	id_proof=[]
	rooms=[]
	for i in list:
		name_of_guest=i.fname+i.lname
		name.append(name_of_guest)
		country.append(i.country)
		town.append(i.town)
		mail.append(i.email)
		phone.append(i.phonenumber)
		in_date.append(i.in_date)
		out_date.append(i.out_date)
		room_count.append(i.room_count)
		guest_count.append(i.guest_count)
		id_proof.append(i.identification)
	guest_details=zip(name,country,town,mail,phone,in_date,out_date,room_count,guest_count,id_proof)
	data={}
	data['guest_details']=guest_details
	return render(request,'reception/guest_list.html',data)