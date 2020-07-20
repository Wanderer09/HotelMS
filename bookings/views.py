import datetime
from django.shortcuts import render,redirect
from .models import booking
from room.models import Room_type as Room_types
from room.models import Room as Rooms
from room.models import services 
from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required
def bookings(request):
	if(request.method=='POST'):
		#data_from_FORM
		in_date=request.POST.get('in_date')
		in_time=request.POST.get('in_time','')
		out_date=request.POST.get('out_date','')
		out_time=request.POST.get('out_time','')
		room_count=request.POST.get('room_count','')
		guest_count=request.POST.get('guest_count','')
		adult_count=request.POST.get('adult_count','')
		children_count=request.POST.get('children_count','')
		country=request.POST.get('country','')
		fname=request.POST.get('fname','')
		lname=request.POST.get('lname','')
		phonenumber=request.POST.get('phonenumber','')
		town=request.POST.get('town','')
		gender=request.POST.get('gender','')
		email=request.POST.get('email','')
		identification=request.POST.get('identification','')
		#convert_into_days
		Checkin = datetime.datetime.strptime(in_date, "%Y-%m-%d").date()
		Checkout = datetime.datetime.strptime(out_date, "%Y-%m-%d").date()
		timedeltaSum = Checkout - Checkin
		StayDuration = timedeltaSum.days
		#Setting_sessions
		request.session['StayDuration']=StayDuration
		request.session['in_date']=in_date
		request.session['out_date']=out_date
		request.session['room_count']=room_count
		request.session['guest_count']=guest_count
		request.session['adult_count']=adult_count
		request.session['children_count']=children_count
		request.session['country']=country
		request.session['fname']=fname
		request.session['lname']=lname
		request.session['phonenumber']=phonenumber
		request.session['town']=town
		request.session['gender']=gender
		request.session['email']=email
		request.session['identification']=identification
		# booking1=booking(in_date=in_date,in_time=in_time,out_date=out_date,out_time=out_time,room_count=room_count,guest_count=guest_count,adult_count=adult_count,children_count=children_count,country=country,fname=fname,lname=lname,phonenumber=phonenumber,town=town,gender=gender,email=email,identification=identification)
		# booking1.save()
		# data={'in_date':in_date,'in_time':in_time,'out_date':out_date,'out_time':out_time,'room_count':room_count,'guest_count':guest_count,'adult_count':adult_count,'children_count':children_count,'country':country,'fname':fname,'lname':lname,'phonenumber':phonenumber,'town':town,'gender':gender,'email':email,'identification':identification}
		return redirect('booking2')
	return render(request,'bookings/booking.html',{})
# @login_required
def booking2(request):
	#Taking_session_Values
	in_date=request.session['in_date']
	out_date=request.session['out_date']
	room_count=request.session['room_count']
	guest_count=request.session['guest_count']
	#Getting_rooms_data
	count=Room_types.objects.all().count()
	room_types=Room_types.objects.all()
	#setting_lists
	room_available_count=[]
	style=[]
	price=[]
	rating=[]
	img=[]
	service=[]
	service_cost=[]
	service_av=[]
	#accessing_rooms_data
	for i in range(1,count+1):
		a=Rooms.objects.filter(room_status='a',room_type_id=i).count()
		room_available_count.append(a)
	for i in room_types:
		style.append(i.room_type)
		price.append(i.room_price)
		rating.append(i.room_rating)
		img.append(i.room_img)
	mylist=zip(style,price,rating,room_available_count,img)
	services_all=services.objects.all()
	for i in services_all:
		service.append(i.service_type)
		service_cost.append(i.service_cost)
		service_av.append(i.service_availability)
	if(request.method=='POST'):
		room_data={}
		service_request=[]
		for j in request.POST.getlist('service_check'):
			service_request.append(j)
		room_data['additional_sevices']=service_request;
		booked_rooms=[]
		booked_rooms_count=[]
		for i in style:
			if request.POST.get(i,False):
			   counter=request.POST.get('count-'+i,False)
			   booked_rooms.append(i)
			   booked_rooms_count.append(int(counter))
		request.session['booked_rooms']=booked_rooms
		request.session['booked_rooms_count']=booked_rooms_count
		request.session['service_request']=service_request			   
		return redirect('booking3')
	mydata={}
	mydata["mylist"]=mylist
	mydata['service_list']=zip(service,service_cost,service_av)
	in_date=request.session['in_date']
	out_date=request.session['out_date']
	room_count=request.session['room_count']
	guest_count=request.session['guest_count']
	mydata['in_date']=in_date
	mydata['out_date']=out_date
	mydata['room_count']=room_count
	mydata['guest_count']=guest_count
	return render(request,'bookings/booking2.html',mydata)
# @login_required
def booking3(request):
	in_date=request.session['in_date']
	out_date=request.session['out_date']
	room_count=request.session['room_count']
	guest_count=request.session['guest_count']
	country=request.session['country']
	fname=request.session['fname']
	lname=request.session['lname']
	StayDuration=request.session['StayDuration']
	phonenumber=request.session['phonenumber']
	town=request.session['town']
	gender=request.session['gender']
	email=request.session['email']
	identification=request.session['identification']
	booked_rooms=request.session['booked_rooms']
	booked_rooms_count=request.session['booked_rooms_count']
	service_request=request.session['service_request']
	my_rooms=list(zip(booked_rooms,booked_rooms_count))
	price_of_rooms=[]
	total_price_rooms=[]
	total_tax=[]
	total_amount=[]
	total_service_cost=0
	service_request_cost=[]
	for i in service_request:
		a=services.objects.filter(service_type=i).values_list('service_cost',flat=True)
		cost_service=int(a[0])
		service_request_cost.append(cost_service)
		total_service_cost+=cost_service
	total=0
	service_request_data=list(zip(service_request,service_request_cost))
	for i,j in my_rooms:
		a=Room_types.objects.filter(room_type=i).values_list('room_price',flat=True)
		cost=int(a[0])
		price_of_rooms.append(cost)
		total_cost=int(cost)*int(j)*int(j)
		total_price_rooms.append(total_cost)
		if(total_cost<1000):
			percentage=0.00
		elif(total_cost>1000 and total_cost<7500):
			percentage=0.12
		else:
			percentage=0.18
		tax=percentage*total_cost
		total_tax.append(tax)
		total_a=total_cost+tax+total_service_cost
		total_amount.append(total_a)
	total=0
	for i in total_amount:
		total+=i

	total_costs=list(zip(booked_rooms,booked_rooms_count,total_price_rooms,total_tax,total_amount))
	request.session['total_costs']=total_costs
	request.session['service_request_data']=service_request_data
	request.session['total']=total
	request.session['total_service_cost']=total_service_cost	
	data={}
	data['in_date']=in_date
	data['out_date']=out_date
	data['room_count']=room_count
	data['guest_count']=guest_count
	data['country']=country
	data['fname']=fname
	data['lname']=lname
	data['phonenumber']=phonenumber
	data['town']=town
	data['gender']=gender
	data['email']=email
	data['identification']=identification
	data['my_rooms']=my_rooms
	data['total']=total
	data['total_costs']=total_costs
	data['total_service_cost']=total_service_cost
	data['service_request_data']=service_request_data
	if(request.POST):
		return redirect('booking4')
	return render(request,'bookings/booking3.html',data)
# @login_required
def booking4(request):
	in_date=request.session['in_date']
	out_date=request.session['out_date']
	room_count=request.session['room_count']
	total_costs=request.session['total_costs']
	service_request_data=request.session['service_request_data']
	total=request.session['total']
	total_service_cost=request.session['total_service_cost']
	mydata={}
	mydata['in_date']=in_date
	mydata['out_date']=out_date
	mydata['room_count']=room_count
	mydata['total_costs']=total_costs
	mydata['total_service_cost']=total_service_cost
	mydata['total']=total
	return render(request,'bookings/booking4.html',mydata)
