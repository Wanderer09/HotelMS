from django.db import models

class Room_type(models.Model):
	room_type=models.CharField(max_length=100);
	room_price=models.PositiveIntegerField();
	smoking_status=models.BooleanField();
	room_rating=models.PositiveIntegerField(default=5)
	room_description=models.CharField(max_length=100);
	number_of_guests=models.PositiveIntegerField();
	show_on_homepage=models.BooleanField(default=False);
	room_img=models.CharField(max_length=500,default='/img/bed-4.jpg')
room_status_choices=[
       ('available','available'),
       ('booked','booked'),
       ('occupied','occupied'),
       ('out_of_order','out Of Order'),
       ('do_not_disturb','do_not_disturb'),
       ('house_use','house_use'),
       ('newly_checked_in','newly_checked_in'),
       ('status_unclear','status_unclear'),
]
class Room(models.Model):
	room_number=models.PositiveIntegerField(primary_key=True);
	room_type=models.ForeignKey(Room_type,on_delete=models.CASCADE,to_field='id');
	room_status=models.CharField(max_length=30,choices=room_status_choices,default='available');
	room_floor=models.PositiveIntegerField();
	housekeeping_status=models.CharField(max_length=100,default='room_cleaned')
	issue=models.CharField(max_length=100,default='no_issues')
	issue_description=models.TextField(blank=True,null=True)
class services(models.Model):
	service_type=models.CharField(max_length=100);
	service_cost=models.PositiveIntegerField();
	service_availability=models.BooleanField(default=True);


