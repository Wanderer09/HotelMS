import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import booking_guest_details,booking_room_details,booking
from room.models import Room_type as Room_types
from room.models import Room as Rooms
from traveldesk.models import pick_drop
from django.utils.translation import get_language
from room.models import services 
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
from django.conf import settings
import json
# Create your views here.
jsonDec = json.decoder.JSONDecoder()
@login_required
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
		request.session['in_time']=in_time
		request.session['out_time']=out_time
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

@login_required
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
	available_room_numbers=[]
	#accessing_rooms_data
	for i in range(1,count+1):
		a=Rooms.objects.filter(room_status='available',room_type_id=i).count()
		room_available_count.append(a)
	for i in room_types:
		style.append(i.room_type)
		price.append(i.room_price)
		rating.append(i.room_rating)
		img.append(i.room_img)

	mylist=list(zip(style,price,rating,room_available_count,img))
	services_all=services.objects.all()
	for i in services_all:
		service.append(i.service_type)
		service_cost.append(i.service_cost)
		service_av.append(i.service_availability)
	if(request.method=='POST'):
		service_request=[]
		booked_rooms=[]
		booked_rooms_count=[]
		booked_rooms_numbers=[]
		for j in request.POST.getlist('service_check'):
			service_request.append(j)
		for i in style:
			style_data=Room_types.objects.get(room_type=i)
			if request.POST.get(i,False):
			   counter=int(request.POST.get('count-'+i,False))
			   available_room_numbers=[]
			   booked_room_numbers=[]
			   available=Rooms.objects.filter(room_status='available',room_type_id=style_data.id)
			   for t in available:
			   	available_room_numbers.append(t.room_number)
			   increment=0
			   for k in range(1,counter+1):
			   	booked_room_numbers.append(available_room_numbers[increment])
			   	increment+=1
			   booked_rooms_numbers.append(booked_room_numbers)
			   booked_rooms.append(i)
			   booked_rooms_count.append(int(counter))
		request.session['booked_rooms_numbers']=booked_rooms_numbers
		request.session['booked_rooms']=booked_rooms
		request.session['booked_rooms_count']=booked_rooms_count
		request.session['service_request']=service_request	   
		return redirect('booking3')
	mydata={}
	mydata["mylist"]=mylist
	mydata['service_list']=list(zip(service,service_cost,service_av))
	in_date=request.session['in_date']
	out_date=request.session['out_date']
	room_count=request.session['room_count']
	guest_count=request.session['guest_count']
	mydata['in_date']=in_date
	mydata['out_date']=out_date
	mydata['room_count']=room_count
	mydata['guest_count']=guest_count
	return render(request,'bookings/booking2.html',mydata)

@login_required
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
	booked_rooms_numbers=request.session['booked_rooms_numbers']
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
	#Service__Amounts
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
    #total__Room__Amounts
	total_costs=list(zip(booked_rooms,booked_rooms_count,total_price_rooms,total_tax,total_amount,booked_rooms_numbers))
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

@login_required
def booking4(request):
	booked_rooms_numbers=request.session['booked_rooms_numbers']
	in_time=request.session['in_time']
	out_time=request.session['out_time']
	in_date=request.session['in_date']
	out_date=request.session['out_date']
	room_count=request.session['room_count']
	guest_count=request.session['guest_count']
	adult_count=request.session['adult_count']
	children_count=request.session['children_count']
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
	total_costs=request.session['total_costs']
	service_request_data=request.session['service_request_data']
	total=request.session['total']
	total_service_cost=request.session['total_service_cost']
	if(request.POST):
		ORDER_ID=Checksum.__id_generator__();
		user=request.user
		payment_type=request.POST.get('radio-box',False)
		guests=booking_guest_details(user=user,in_date=in_date,in_time=in_time,out_date=out_date,out_time=out_time,room_count=room_count,guest_count=guest_count,adult_count=adult_count,children_count=children_count,country=country,fname=fname,lname=lname,phonenumber=phonenumber,town=town,gender=gender,email=email,identification=identification)
		guests.save()
		room=booking_room_details(user=user,booking_guest_details=guests,Room_details=json.dumps(total_costs),service_details=json.dumps(service_request_data),payment_type=payment_type)
		room.save()
		bookings=booking(amount=total,booking_guest_details=guests,booking_room_details=room,user=user,order_id=ORDER_ID)
		bookings.save()
		booking_room_detail=booking_room_details.objects.all()
		booking_guest_detail=booking_guest_details.objects.all()
		temp=1
		for i in booking_room_detail:
			service_detail=jsonDec.decode(i.service_details)
			for service,cost in service_detail:
				if('Pick_Drop' in service):
					guest=booking_guest_details.objects.get(id=i.booking_guest_details_id)
					room=jsonDec.decode(i.Room_details)
					for a,b,c,d,e,room_number in room:
						for j in room_number:
							pick_drop.objects.create(name=guest.fname+''+guest.lname,room_number=j,contact=guest.phonenumber,email=guest.email)
		MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
		MERCHANT_ID = settings.PAYTM_MERCHANT_ID
		get_lang = "/" + get_language() if get_language() else ''
		CALLBACK_URL = settings.HOST_URL + get_lang + settings.PAYTM_CALLBACK_URL
		param_dict={
			'MID':MERCHANT_ID,
            'ORDER_ID':ORDER_ID,
            'TXN_AMOUNT':str(total),
            'CUST_ID':'email',
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':settings.PAYTM_WEBSITE,
            'CHANNEL_ID':'WEB',
            # 'CALLBACK_URL':CALLBACK_URL,
            'CALLBACK_URL':'http://127.0.0.1:8000/bookings/response/',
		}
		param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
		session_keys = list(request.session.keys())
		for key in session_keys:
			del request.session[key]
		return render(request, 'bookings/paytm.html', {'param_dict': param_dict})

	mydata={}
	mydata['in_date']=in_date
	mydata['out_date']=out_date
	mydata['room_count']=room_count
	mydata['total_costs']=total_costs
	mydata['total_service_cost']=total_service_cost
	mydata['total']=total
	return render(request,'bookings/booking4.html',mydata)

@csrf_exempt
def response(request):
	MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
	MERCHANT_ID = settings.PAYTM_MERCHANT_ID
	form = request.POST
	response_dict = {}
	for i in form.keys():
		response_dict[i] = form[i]
		if i == 'CHECKSUMHASH':
			checksum = form[i]

	verify = Checksum.verify_checksum(response_dict,MERCHANT_KEY, checksum)
	if verify:
		if response_dict['RESPCODE'] == '01':
			book=booking.objects.get(order_id=response_dict['ORDERID'])
			rooms=booking_room_details.objects.get(id=book.booking_room_details_id)
			booked_rooms=jsonDec.decode(rooms.Room_details)
			for room,count,totalcost,tax,amount,number in booked_rooms:
				for i in number:
					room=Rooms.objects.get(room_number=i)
					room.room_status='booked'
					room.save()
			book.payment_status='successful'
			book.save()
			print('Order Successful')
		else:
			for room,count,totalcost,tax,amount,number in booked_rooms:
				for i in number:
					room=Rooms.objects.get(room_number=i)
					room.room_status='available'
					room.save()
			book.payment_status='failed'
			book.save()
			print('order was not successful because' + response_dict['RESPMSG'])
	return render(request, 'bookings/paymentstatus.html', {'response': response_dict})
	
	#return HttpResponse("done")
	#pass
