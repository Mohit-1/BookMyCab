from rest_framework import serializers
from .models import User, Cab, Booking

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'first_name', 'last_name', 'email', 'contact_number', 'location', 'is_driver')

class CabSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cab
		fields = '__all__'	

class BookingSerializer(serializers.ModelSerializer):	
	class Meta:
		model = Booking
		fields = '__all__'