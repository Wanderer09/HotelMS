from django.shortcuts import render,redirect
from .models import vehicle,driver_details,vehicle_bookings,pick_drop
from bookings.models import booking,booking_room_details,booking_guest_details
import json
jsonDec = json.decoder.JSONDecoder()





##################################
# Bookings Page
##################################





def traveldesk_home(request):
	if(vehicle.objects.all().count()==0):
		vehicle.objects.create(vehicle='car',vehicle_name='Hundai',registered_number='AP27 4444',vehicle_category='sedan_car',vehicle_status='available')
		vehicle.objects.create(vehicle='car',vehicle_name='Ford',registered_number='AP27 4890',vehicle_category='prime_car',vehicle_status='available')
		vehicle.objects.create(vehicle='car',vehicle_name='Bmw',registered_number='AP27 4567',vehicle_category='sedan_car',vehicle_status='available')
		vehicle.objects.create(vehicle='car',vehicle_name='toyota',registered_number='AP27 3456',vehicle_category='mini_car',vehicle_status='available')
		vehicle.objects.create(vehicle='Bike',vehicle_name='pulser',registered_number='AP27 8769',vehicle_category='Moter Bike',vehicle_status='available')
		vehicle.objects.create(vehicle='Bike',vehicle_name='Bullet',registered_number='AP27 2345',vehicle_category='Moter Bike',vehicle_status='available')
		vehicle.objects.create(vehicle='Bike',vehicle_name='Bullet',registered_number='AP27 1005',vehicle_category='Moter Bike',vehicle_status='available')
		vehicle.objects.create(vehicle='Bike',vehicle_name='Bullet',registered_number='AP27 1004',vehicle_category='Moter Bike',vehicle_status='available')
		vehicle.objects.create(vehicle='Bike',vehicle_name='Bullet',registered_number='AP27 1003',vehicle_category='Moter Bike',vehicle_status='available')
		vehicle.objects.create(vehicle='Bike',vehicle_name='Bullet',registered_number='AP27 1002',vehicle_category='Moter Bike',vehicle_status='available')
		vehicle.objects.create(vehicle='Bike',vehicle_name='Bullet',registered_number='AP27 1001',vehicle_category='Moter Bike',vehicle_status='available')
		vehicle.objects.create(vehicle='Bike',vehicle_name='Bullet',registered_number='AP27 1000',vehicle_category='Moter Bike',vehicle_status='available')
		vehicle.objects.create(vehicle='Bike',vehicle_name='pulser',registered_number='AP27 3450',vehicle_category='Moter Bike',vehicle_status='available')
		vehicle.objects.create(vehicle='car',vehicle_name='Hundai',registered_number='AP27 4770',vehicle_category='prime_car',vehicle_status='available')
		vehicle.objects.create(vehicle='car',vehicle_name='Hundai',registered_number='AP27 4779',vehicle_category='zeep',vehicle_status='available')
		vehicle.objects.create(vehicle='car',vehicle_name='Hundai',registered_number='AP27 4771',vehicle_category='mini_car',vehicle_status='available')
		vehicle.objects.create(vehicle='car',vehicle_name='Hundai',registered_number='AP27 4774',vehicle_category='zeep',vehicle_status='available')
		vehicle.objects.create(vehicle='car',vehicle_name='Hundai',registered_number='AP27 4773',vehicle_category='zeep',vehicle_status='available')
		vehicle.objects.create(vehicle='car',vehicle_name='Tata',registered_number='AP27 4709',vehicle_category='mini_car',vehicle_status='available')
		vehicle.objects.create(vehicle='car',vehicle_name='Tata',registered_number='AP27 4789',vehicle_category='luxury_car',vehicle_status='available')
		vehicle.objects.create(vehicle='car',vehicle_name='Tata',registered_number='AP27 4734',vehicle_category='luxury_car',vehicle_status='available')
		vehicle.objects.create(vehicle='car',vehicle_name='Tata',registered_number='AP27 4756',vehicle_category='luxury_car',vehicle_status='available')
		vehicle.objects.create(vehicle='car',vehicle_name='benz',registered_number='AP27 4999',vehicle_category='luxury_car',vehicle_status='available')
		vehicle.objects.create(vehicle='car',vehicle_name='Bmw',registered_number='AP27 4000',vehicle_category='luxury_car',vehicle_status='available')
	if(driver_details.objects.all().count()==0):
		driver_details.objects.create(driver_name='ram',driver_phonenumber='9542856767',driver_age='22',driver_gender='male',driver_status='available')
		driver_details.objects.create(driver_name='laxman',driver_phonenumber='9542456789',driver_age='32',driver_gender='male',driver_status='available')
		driver_details.objects.create(driver_name='sudheer',driver_phonenumber='9542688790',driver_age='20',driver_gender='male',driver_status='available')
		driver_details.objects.create(driver_name='pavan',driver_phonenumber='9542854565',driver_age='27',driver_gender='male',driver_status='available')
		driver_details.objects.create(driver_name='santhi',driver_phonenumber='9542345678',driver_age='28',driver_gender='male',driver_status='available')
		driver_details.objects.create(driver_name='raju',driver_phonenumber='9542567889',driver_age='29',driver_gender='male',driver_status='available')
		driver_details.objects.create(driver_name='ramu',driver_phonenumber='9542000000',driver_age='30',driver_gender='male',driver_status='available')
		driver_details.objects.create(driver_name='ravi',driver_phonenumber='9541234567',driver_age='21',driver_gender='male',driver_status='available')
		driver_details.objects.create(driver_name='rani',driver_phonenumber='9542754567',driver_age='32',driver_gender='female',driver_status='available')
		driver_details.objects.create(driver_name='anusha',driver_phonenumber='956789000',driver_age='25',driver_gender='female',driver_status='available')
		driver_details.objects.create(driver_name='ramya',driver_phonenumber='9556789090',driver_age='27',driver_gender='female',driver_status='available')
		driver_details.objects.create(driver_name='rajesh',driver_phonenumber='9545678900',driver_age='21',driver_gender='male',driver_status='available')
		driver_details.objects.create(driver_name='sai',driver_phonenumber='9544567890',driver_age='27',driver_gender='male',driver_status='available')
		driver_details.objects.create(driver_name='siva',driver_phonenumber='9542856799',driver_age='20',driver_gender='male',driver_status='available')
	vehicle_data=vehicle.objects.filter(vehicle_status='available')
	vehicle_type=[]
	vehicle_category=[]
	vehicle_number=[]
	for i in vehicle_data:
		if i.vehicle not in vehicle_type:
			vehicle_type.append(i.vehicle)
		vehicle_number.append(i.registered_number)
		if i.vehicle_category not in vehicle_category:
			vehicle_category.append(i.vehicle_category)
	driver_data=driver_details.objects.filter(driver_status='available')
	driver_name=[]
	driver_id=[]
	for i in driver_data:
		driver_name.append(i.driver_name)
		driver_id.append(i.id)
	driver=list(zip(driver_id,driver_name))
	if request.method=='POST':
		name=request.POST.get('name')
		room_number=request.POST.get('room_number')
		type_vehicle=request.POST.get('type')
		category_vehicle=request.POST.get('category')
		number_vehicle=request.POST.get('number')
		time=request.POST.get('time')
		driving=request.POST.get('driving')
		driver_alloted=request.POST.get('driver')
		if(name!='' and room_number!='' and type_vehicle!=None and category_vehicle!=None and number_vehicle!=None and time!='' and driving!=None):
			if(driving!='self'):
				driver_status=driver_details.objects.get(id=driver_alloted)
				driver_status.driver_status='booked'
				driver_status.save(update_fields=['driver_status'])
			else:
				driver_alloted='None'
			vehicle_status=vehicle.objects.get(registered_number=number_vehicle)
			vehicle_status.vehicle_status='booked'
			vehicle_status.save(update_fields=['vehicle_status'])
			vehicle_bookings.objects.create(guest_name=name,room_number=room_number,vehicle=type_vehicle,vehicle_type=category_vehicle,vehicle_number=number_vehicle,driver_type=driving,driver_alloted=driver_alloted,time_alloted=time)
			return redirect('rent',permanent=True)
		if(name!='' and room_number!='' and type_vehicle!=None and category_vehicle!=None and number_vehicle!=None):
			vehicle_data=vehicle.objects.filter(vehicle_status='available',vehicle=type_vehicle)
			vehicle_data2=vehicle.objects.filter(vehicle_status='available',vehicle=type_vehicle,vehicle_category=category_vehicle)
			driver_data=driver_details.objects.filter(driver_status='available')
			vehicle_category=[]
			vehicle_number=[]
			driver_name=[]
			for i in driver_data:
				if i.driver_name not in driver_name:
					driver_name.append(i.driver_name)
			for i in vehicle_data:
				if i.vehicle_category not in vehicle_category:
					vehicle_category.append(i.vehicle_category)
			for i in vehicle_data2:
				if i.registered_number not in vehicle_number:
					vehicle_number.append(i.registered_number)
			data={}
			data['name']=name
			data['type']=vehicle_type
			data['room_number']=room_number
			data['type_vehicle']=str(type_vehicle)
			data['category_vehicle']=str(category_vehicle)
			data['number_vehicle']=str(number_vehicle)
			data['select']='selected'
			data['driver']=driver
			data['number']=vehicle_number
			data['category']=vehicle_category
			return render(request,'traveldesk/travel.html',data)
		if(name!='' and room_number!='' and type_vehicle!=None and category_vehicle!=None):
			vehicle_data=vehicle.objects.filter(vehicle_status='available',vehicle=type_vehicle)
			vehicle_data2=vehicle.objects.filter(vehicle_status='available',vehicle=type_vehicle,vehicle_category=category_vehicle)
			vehicle_category=[]
			vehicle_number=[]
			for i in vehicle_data:
				if i.vehicle_category not in vehicle_category:
					vehicle_category.append(i.vehicle_category)
			for i in vehicle_data2:
				if i.registered_number not in vehicle_number:
					vehicle_number.append(i.registered_number)
			data={}
			data['name']=name
			data['type']=vehicle_type
			data['room_number']=room_number
			data['type_vehicle']=str(type_vehicle)
			data['category_vehicle']=str(category_vehicle)
			data['select']='selected'
			data['number']=vehicle_number
			data['driver']=driver
			data['category']=vehicle_category
			return render(request,'traveldesk/travel.html',data)
		if(name!='' and room_number!='' and type_vehicle!=None):
			vehicle_data=vehicle.objects.filter(vehicle_status='available',vehicle=type_vehicle)
			vehicle_category=[]
			vehicle_number=[]
			for i in vehicle_data:
				if i.vehicle_category not in vehicle_category:
					vehicle_category.append(i.vehicle_category)
				vehicle_number.append(i.registered_number)
			data={}
			data['name']=name
			data['type']=vehicle_type
			data['room_number']=room_number
			data['type_vehicle']=str(type_vehicle)
			data['select']='selected'
			data['number']=vehicle_number
			data['category']=vehicle_category
			data['driver']=driver
			return render(request,'traveldesk/travel.html',data)
		# if(name=='' and room_number==''):
		# 	data['error_name']=1
		# 	data['error_room']=1
		# 	data['hidden']='hidden'
		# 	data['visible']='visible'
		# 	return render(request,'traveldesk/travel.html',data)
		# if(name==''):
		# 	data['error_name']=1
		# 	data['room_number']=room_number
		# 	data['hidden']='hidden'
		# 	data['visible']='visible'
		# 	return render(request,'traveldesk/travel.html',data)
		# if(room_number==''):
		# 	data['error_room']=1
		# 	data['name']=name
		# 	data['hidden']='hidden'
		# 	data['visible']='visible'
		# 	return render(request,'traveldesk/travel.html',data)
	mydata={}
	mydata['type']=vehicle_type
	mydata['number']=vehicle_number
	mydata['category']=vehicle_category
	mydata['driver']=driver
	return render(request,'traveldesk/travel.html',mydata)












#############################
#rental_status Page
#############################











def rent(request):
	bookings=vehicle_bookings.objects.all()
	name=[]
	room_number=[]
	vehicle_type=[]
	vehicle_category=[]
	vehicle_number=[]
	driving=[]
	driver_alloted=[]
	time=[]
	for i in bookings:
		name.append(i.guest_name)
		room_number.append(i.room_number)
		vehicle_type.append(i.vehicle)
		vehicle_category.append(i.vehicle_type)
		vehicle_number.append(i.vehicle_number)
		driving.append(i.driver_type)
		driver_alloted.append(i.driver_alloted)
		time.append(i.time_alloted)
	data=list(zip(name,room_number,vehicle_type,vehicle_category,vehicle_number,driving,driver_alloted,time))
	mydata={}
	mydata['data']=data
	return render(request,'traveldesk/rent.html',mydata)




#########################
#Pick an Drop
#########################





def pick(request):
	pick_drop_details=pick_drop.objects.all()
	vehicle_data=vehicle.objects.filter(vehicle_status='available')
	driver_detail=driver_details.objects.filter(driver_status='available')
	driver_list=['None']
	vehicle_category=['None']
	vehicle_number=['None']
	driver_id=['']
	for i in driver_detail:
		driver_id.append(i.id)
		driver_list.append(i.driver_name)
	for i in vehicle_data:
		if i.vehicle_category not in vehicle_category:
			vehicle_category.append(i.vehicle_category)
	name=[]
	number=[]
	mail=[]
	phn=[]
	details_id=[]
	pick=[]
	drop=[]
	time=[]
	category=[]
	registered_number=[]
	driver=[]
	status=[]
	number_list=[]
	for i in pick_drop_details:
		details_id.append(i.id)
		number.append(i.room_number)
		name.append(i.name)
		mail.append(i.email)
		phn.append(i.contact)
		pick.append(i.pick_location)
		drop.append(i.drop_location)
		time.append(i.time)
		category.append(i.vehicle_category)
		vehicle_number=[]
		d=vehicle.objects.filter(vehicle_category=i.vehicle_category,vehicle_status='available')
		for v in d:
			vehicle_number.append(v.registered_number)
		number_list.append(vehicle_number)
		registered_number.append(i.registered_number)
		driver.append(i.driver)
		status.append(i.status)
	data=list(zip(details_id,name,number,phn,mail,pick,drop,time,category,registered_number,driver,status,number_list))
	if request.method=='POST':
		vehicle_number=['None']
		for i in details_id:
			x=pick_drop.objects.get(id=i)
			if (request.POST.get('status-'+str(i))):
				q=request.POST.get('status-'+str(i))
				x.status=q
				x.save(update_fields=['status'])
			if (request.POST.get('vehicle-'+str(i))):
				w=request.POST.get('vehicle-'+str(i))
				x.registered_number=w
				x.save(update_fields=['registered_number'])
			if (request.POST.get('category-'+str(i))):
				e=request.POST.get('category-'+str(i))
				x.vehicle_category=e 
				x.save(update_fields=['vehicle_category'])
			if (request.POST.get('driver-'+str(i))):
				f=request.POST.get('driver-'+str(i))
				x.driver=f
				x.save(update_fields=['driver'])
			if (request.POST.get('pick-'+str(i))):
				g=request.POST.get('pick-'+str(i))
				x.pick_location=g
				x.save(update_fields=['pick_location'])
			if (request.POST.get('drop-'+str(i))):
				h=request.POST.get('drop-'+str(i))
				x.drop_location=h
				x.save(update_fields=['pick_location'])
			if (request.POST.get('time-'+str(i))):
				j=request.POST.get('time-'+str(i))
				x.time=j
				x.save(update_fields=['time'])
		return redirect('pick',permanent=True)
	mydata={}
	mydata['data']=data
	mydata['select']='selected'
	mydata['driver_list']=list(zip(driver_id,driver_list))
	mydata['vehicle_number']=vehicle_number
	mydata['vehicle_category']=vehicle_category
	mydata['pick_drop_status']=['unclear','booked','OnWork','Closed','Cancelled']
	return render(request,'traveldesk/pick.html',mydata)








#########################
#Driver Status
#########################











def driver(request):
	driver=driver_details.objects.all()
	vehicle_data=vehicle.objects.all()
	registered_number=[]
	vehicle_status=[]
	vehicle_type=[]
	vehicle_allocated=[]
	vehicle_number=[]
	for i in vehicle_data:
		if i.vehicle_category not in vehicle_type:
			vehicle_type.append(i.vehicle_category)
		vehicle_status.append(i.vehicle_status)
		registered_number.append(i.registered_number)
	driverid=[]
	name=[]
	phone=[]
	status=[]
	for i in driver:
		driverid.append(i.id)
		name.append(i.driver_name)
		phone.append(i.driver_phonenumber)
		status.append(i.driver_status)
		if i.driver_status =='booked':
			k=vehicle_bookings.objects.get(driver_alloted=i.id)
			vehicle_allocated.append(k.vehicle_type)
			vehicle_number.append(k.vehicle_number)
		else:
			vehicle_allocated.append('None')
			vehicle_number.append('None')
	if request.method=='POST':
		for i in driverid:
			x=driver_details.objects.get(id=i)
			if (request.POST.get('status-'+str(i))):
				q=request.POST.get('status-'+str(i))
				if(q=='booked'):
					return redirect('driver',permanent=True)
				x.driver_status=q
				x.save(update_fields=['driver_status'])
		return redirect('driver',permanent=True)
	driver_data=list(zip(driverid,name,phone,status,vehicle_allocated,vehicle_number))
	mydata={}
	mydata['driver']=driver_data
	mydata['available']='available'
	mydata['booked']='booked'
	mydata['on_leave']='on_leave'
	mydata['select']='selected'
	return render(request,'traveldesk/driver.html',mydata)



# driver=driver_details.objects.all()
# 	vehicle_data=vehicle.objects.all()
# 	registered_number=[]
# 	vehicle_status=[]
# 	vehicle_type=[]
# 	for i in vehicle_data:
# 		if i.vehicle_category not in vehicle_type:
# 			vehicle_type.append(i.vehicle_category)
# 		vehicle_status.append(i.vehicle_status)
# 	driverid=[]
# 	name=[]
# 	phone=[]
# 	status=[]
# 	alloted=[]
# 	number=[]
# 	for i in driver:
# 		driverid.append(i.id)
# 		name.append(i.driver_name)
# 		phone.append(i.driver_phonenumber)
# 		status.append(i.driver_status)
# 		alloted.append(i.vehicle_alloted)
# 		k=vehicle.objects.filter(vehicle_category=i.vehicle_alloted)
# 		numbers=[]
# 		for j in k:
# 			numbers.append(j.registered_number)
# 		number.append(numbers)
# 		registered_number.append(i.number)
# 		s=vehicle.objects.get(registered_number=i.number)
# 		i.vehicle_number_id=s.id
# 		i.save(update_fields=['vehicle_number_id'])
# 	if request.method=='POST':
# 		for i in driverid:
# 			x=driver_details.objects.get(id=i)
# 			if (request.POST.get('status-'+str(i))):
# 				q=request.POST.get('status-'+str(i))
# 				x.driver_status=q
# 				x.save(update_fields=['driver_status'])
# 			if (request.POST.get('vehicle-'+str(i))):
# 				w=request.POST.get('vehicle-'+str(i))
# 				x.vehicle_alloted=w
# 				x.save(update_fields=['vehicle_alloted'])
# 			if (request.POST.get('number-'+str(i))):
# 				e=request.POST.get('number-'+str(i))
# 				x.number=e 
# 				x.save(update_fields=['number'])
# 		return redirect('driver',permanent=True)
# 	driver_data=list(zip(driverid,name,phone,status,alloted,number,registered_number))
# 	mydata={}
# 	mydata['driver']=driver_data
# 	mydata['registered_number']=registered_number
# 	mydata['vehicle_type']=vehicle_type
# 	mydata['vehicle']=vehicle_data
# 	mydata['available']='available'
# 	mydata['booked']='booked'
# 	mydata['on_leave']='on_leave'
# 	mydata['select']='selected'
# 	for i in alloted:
# 		mydata[i]=str(i)
# 	return render(request,'traveldesk/driver.html',mydata)




##########################
#vehicle_status Page
##########################




def car(request):
	vehicle_data=vehicle.objects.all()
	vehicleid=[]
	vehicle_type=[]
	vehicle_name=[]
	vehicle_category=[]
	vehicle_number=[]
	vehicle_status=[]
	for i in vehicle_data:
		vehicleid.append(i.id)
		vehicle_type.append(i.vehicle)
		vehicle_name.append(i.vehicle_name)
		vehicle_number.append(i.registered_number)
		vehicle_category.append(i.vehicle_category)
		vehicle_status.append(i.vehicle_status)
	data=list(zip(vehicleid,vehicle_type,vehicle_name,vehicle_number,vehicle_category,vehicle_status))
	if(request.method == 'POST'):
		for i in vehicleid:
			x=vehicle.objects.get(id=i)
			if(request.POST.get(str(i))):
				value=request.POST.get(str(i))
				x.vehicle_status=value
				x.save(update_fields=['vehicle_status'])
		return redirect('car',permanent=True)

	mydata={}
	mydata['vehicle_details']=data
	mydata['select']='selected'
	mydata['booked']='booked'
	mydata['available']='available'
	mydata['out_of_order']='out_of_order'
	mydata['under_service']='under_service'
	return render(request,'traveldesk/car.html',mydata)