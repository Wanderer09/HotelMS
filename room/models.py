from django.db import models

class Room_type(models.Model):
	room_type=models.CharField(max_length=100);
	room_price=models.PositiveIntegerField();
	smoking_status=models.BooleanField();
	room_description=models.CharField(max_length=100);
	number_of_guests=models.PositiveIntegerField();
room_status_choices=[
       ('a','Available'),
       ('na','Not_Available'),
       ('r','Reserved'),
       ('m','Maitenance'),
       ('o','Other')
]
class Room(models.Model):
	room_number=models.PositiveIntegerField(primary_key=True);
	room_type=models.ForeignKey(Room_type,on_delete=models.CASCADE);
	room_status=models.CharField(max_length=2,choices=room_status_choices,default='a');
	room_floor=models.PositiveIntegerField();


