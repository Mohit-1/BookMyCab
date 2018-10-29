from django.db import models
from django.contrib.auth.models import AbstractUser 	

# Create your models here.
class User(AbstractUser):
	is_driver = models.BooleanField(default=False)
	contact_number = models.CharField(max_length=10, unique=True)
	location = models.CharField(max_length=30)

class Cab(models.Model):
	cab_name = models.CharField(max_length=20)
	driver = models.OneToOneField('bookings.User', on_delete=models.CASCADE)
	is_booked = models.BooleanField(default=False)

	def __str__(self):
		return self.cab_name

class Booking(models.Model):
	cab = models.ForeignKey('bookings.Cab', on_delete=models.CASCADE)
	user = models.ForeignKey('bookings.User', on_delete=models.CASCADE)
	book_time = models.DateTimeField(auto_now_add=True, editable=False)

	def __str__(self):
		return self.cab.cab_name + "-" + self.user.username