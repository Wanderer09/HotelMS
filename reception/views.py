from django.shortcuts import render,redirect
from bookings.models import booking_guest_details,booking_room_details
from room.models import Room,Room_type
from home.models import Contact
import json
import datetime
jsonDec = json.decoder.JSONDecoder()

# Create your views here.
def reception_home(request):
	return render(request,'reception/reception_home.html')
def room_status(request):		
	data=Room.objects.all()
	room_number=[]
	room_status_list=[]
	room_type=[]
	housekeeping_status=[]
	for i in data:
		room_number.append(i.room_number)
		room_status_list.append(i.room_status)
		k=Room_type.objects.get(id=i.room_type_id)
		room_type.append(k.room_type)
		housekeeping_status.append(i.housekeeping_status)
	mydata=list(zip(room_number,room_status_list,room_type,housekeeping_status))
	if(request.method=='POST'):
		for i in room_number:
			i=str(i)
			if(request.POST.get(i,False)):
				room=Room.objects.get(room_number=i)
				value=request.POST.get(i)
				room.room_status=value
				room.save(update_fields=['room_status'])
			j=i+'-status'
			if(request.POST.get(j,False)):
				room=Room.objects.get(room_number=i)
				value=request.POST.get(j)
				room.housekeeping_status=value
				room.save(update_fields=['housekeeping_status'])
		return redirect('room_status',permanent=True)
	room_data={}
	room_data['mydata']=mydata
	room_data['available']='available'
	room_data['booked']='booked'
	room_data['occupied']='occupied'
	room_data['out_of_order']='out_of_order'
	room_data['house_use']='house_use'
	room_data['do_not_disturb']='do_not_disturb'
	room_data['newly_checked_in']='newly_checked_in'
	room_data['checked_out']='checked_out'
	room_data['status_unclear']='status_unclear'
	room_data['occupied_to_be_cleaned']='occupied_to_be_cleaned'
	room_data['vaccant_to_be_cleaned']='vaccant_to_be_cleaned'
	room_data['room_cleaned']='room_cleaned'
	room_data['onqueue']='onqueue'
	room_data['select']='selected'
	return render(request,'reception/room_status.html',room_data)
def maintenance(request):
	data=Room.objects.all()
	room_number=[]
	room_type=[]
	room_status_list=[]
	housekeeping_status=[]
	room_issue=[]
	room_issue_description=[]
	for i in data:
		room_number.append(i.room_number)
		room_status_list.append(i.room_status)
		room_issue.append(i.issue)
		room_issue_description.append(i.issue_description)
		k=Room_type.objects.get(id=i.room_type_id)
		room_type.append(k.room_type)
		housekeeping_status.append(i.housekeeping_status)
	mydata=list(zip(room_number,room_status_list,room_type,housekeeping_status,room_issue,room_issue_description))
	if(request.method=='POST'):
		for i in room_number:
			i=str(i)
			if(request.POST.get(i,False)):
				room=Room.objects.get(room_number=i)
				value=request.POST.get(i)
				room.issue=value
				room.save(update_fields=['issue'])
			j=i+'-description'
			if(request.POST.get(j,False)):
				room=Room.objects.get(room_number=i)
				value=request.POST.get(j)
				room.issue_description=value
				room.save(update_fields=['issue_description'])
		return redirect('maintenance',permanent=True)
	room_data={}
	room_data['electrical_issue']='electrical_issue'
	room_data['plumbing_issue']='plumbing_issue'
	room_data['furniture_issue']='furniture_issue'
	room_data['renovation']='renovation'
	room_data['no_issues']='no_issues'
	room_data['select']='selected'
	room_data['empty']=''
	room_data['mydata']=mydata
	return render(request,'reception/maintenance.html',room_data)
def customer(request):
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
	mydata={}
	mydata['country']=country
	mydata['fname']=fname
	mydata['lname']=lname
	mydata['phonenumber']=phonenumber
	mydata['town']=town
	mydata['gender']=gender
	mydata['email']=email
	mydata['identification']=identification
	return render(request,'reception/customer.html',mydata)
def bookroom(request):
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
		user=request.user

		guests=booking_guest_details(user=user,in_date=in_date,in_time=in_time,out_date=out_date,out_time=out_time,room_count=room_count,guest_count=guest_count,adult_count=adult_count,children_count=children_count,country=country,fname=fname,lname=lname,phonenumber=phonenumber,town=town,gender=gender,email=email,identification=identification)
		# guests.save()
		return redirect('customer',permanent=True)
	return render(request,'reception/bookroom.html')
def enquiry(request):
	data=Contact.objects.all()
	date=[]
	time=[]
	name=[]
	phonenumber=[]
	email=[]
	message=[]
	for i in data:
		date.append(i.date)
		time.append(i.time)
		name.append(i.name)
		phonenumber.append(i.phone)
		email.append(i.email)
		message.append(i.desc)
	mydata={}
	mydata['enquiry_data']=list(zip(date,time,name,phonenumber,email,message))
	return render(request,'reception/enquiry.html',mydata)
def guest_list(request):
	lists=booking_guest_details.objects.all()
	print(lists)
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
	booked_room_details=[]
	for i in lists:
		rooms=[]
		room_number=[]
		room_data=booking_room_details.objects.get(booking_guest_details_id=i.id)
		k=jsonDec.decode(room_data.Room_details)
		for room,count,totalcost,tax,amount,number in k:
			# for i in number:
			rooms.append(room)
			room_number.append(number)
		booked_room_details.append(list
			(zip(rooms,room_number)))
		print(room_number)
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
	guest_details=zip(name,country,town,mail,phone,in_date,out_date,room_count,guest_count,id_proof,booked_room_details)
	data={}
	data['guest_details']=guest_details
	return render(request,'reception/guest_list.html',data)