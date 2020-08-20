from django.shortcuts import render
from room.models import Room,Room_type
from bookings.models import booking,booking_guest_details
from collections import Counter
# import matplotlib.pyplot as plt, mpld3
# Create your views here.
def restro_manager(request):
	return render(request,'manager/restro_manager.html',{})
def hotel_manager(request):
	booking_details=booking.objects.all()
	week1=[]
	week2=[]
	week3=[]
	week4=[]
	month_data=[]
	room_numbers=[]
	booked_rooms=[]
	guests_id=[]
	guests_count=0
	total_rooms_booked=booking.objects.filter(status='closed').count()
	for i in Room.objects.all():
		room_numbers.append(i.room_number)
	for i in booking.objects.filter(status='closed'):
		if i.booking_guest_details_id not in guests_id:
			guests_id.append(i.booking_guest_details_id)
			guests=booking_guest_details.objects.get(id=i.booking_guest_details_id)
			guests_count=guests_count+int(guests.guest_count)
	for i in booking_details:
		if(i.room not in booked_rooms):
			booked_rooms.append(i.room)
	for i in booking_details:
		made_on=str(i.made_on)
		month=int(made_on[5:7])
		date=int(made_on[8:10])
		if date in [1,2,3,4,5,6,7]:
			week1.append(i.status)
		if date in [8,9,10,11,12,13,14]:
			week2.append(i.status)
		if date in [15,16,17,18,19,20,21]:
			week3.append(i.status)
		if date in [22,23,24,25,26,27,28,29,30,31]:
			week4.append(i.status)
		if(month==8):
			month_data.append(i.status)
		for j in room_numbers:
			if(j not in booked_rooms):
				month_data.append('vaccant')
	month_counter=Counter(month_data)
	month_booked_count=month_counter['booked']
	month_cancelled_count=month_counter['cancelled']
	month_vaccant_count=month_counter['vaccant']
	booked_percentage=(month_counter['booked']/len(month_data))*100
	cancelled_percentage=(month_counter['cancelled']/len(month_data))*100
	vaccant_percentage=(month_counter['vaccant']/len(month_data))*100
	eek4_percentage=(len(week4)/len(month_data))*100
	week1_data=Counter(week1)
	week2_data=Counter(week2)
	week3_data=Counter(week3)
	week4_data=Counter(week4)
	week1_booked=week1_data['closed']
	week2_booked=week2_data['closed']
	week3_booked=week3_data['closed']
	week4_booked=week4_data['closed']
	week1_cancelled=week1_data['cancelled']
	week2_cancelled=week2_data['cancelled']
	week3_cancelled=week3_data['cancelled']
	week4_cancelled=week4_data['cancelled']
	week1_percentage=((week1_booked)/len(month_data))*100
	week2_percentage=((week2_booked)/len(month_data))*100
	week3_percentage=((week3_booked)/len(month_data))*100
	week4_percentage=((week3_booked)/len(month_data))*100
	x=0
	colors=['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5', '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f', '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']
	room_types=Room_type.objects.all()
	type_list=[]
	number_list=[]
	color_list=[]
	for i in room_types:
		count=0
		type_list.append(i.room_type)
		k=Room.objects.filter(room_type=i.id)
		for i in k:
			count=count+1
		number_list.append(count)
		color_list.append(colors[x])
		x=x+1

	type_data=list(zip(type_list,number_list,color_list))
	data={}
	data['type_data']=type_data
	data['week1_booked']=week1_booked
	data['week2_booked']=week2_booked
	data['week3_booked']=week3_booked
	data['week4_booked']=week4_booked
	data['week1_cancelled']=week1_cancelled
	data['week2_cancelled']=week2_cancelled
	data['week3_cancelled']=week3_cancelled
	data['week4_cancelled']=week4_cancelled
	data['booked_percentage']=booked_percentage
	data['cancelled_percentage']=cancelled_percentage
	data['vaccant_percentage']=vaccant_percentage
	data['week1_percentage']=week1_percentage
	data['week2_percentage']=week2_percentage
	data['week3_percentage']=week3_percentage
	data['week4_percentage']=week4_percentage
	data['booked_rooms_count']=total_rooms_booked
	data['guests_count']=guests_count
	data['rooms_count']=Room.objects.all().count

	# fig=plt.figure()
	# plt.plot([1,2,3],[4,5,1])
	# fig = mpld3.fig_to_html(fig)
	# data={'plt':fig}
	return render(request,'manager/hotel-manager.html',data)     	
