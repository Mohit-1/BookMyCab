from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from .models import User, Cab, Booking
from .serializers import UserSerializer, CabSerializer, BookingSerializer
from rest_framework.response import Response

# Create your views here.
class ListCreateUsers(generics.ListCreateAPIView):
	serializer_class = UserSerializer
	queryset = User.objects.all()

class ListCreateCabs(generics.ListCreateAPIView):
	serializer_class = CabSerializer
	queryset = Cab.objects.all()

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		user = serializer.validated_data['driver']

		if not user.is_driver:
		 	return Response(status=status.HTTP_400_BAD_REQUEST)

		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class RetrieveUpdateDestroyUser(generics.RetrieveUpdateDestroyAPIView):	
	serializer_class = UserSerializer
	queryset = User.objects.all()	

class RetrieveUpdateDestroyCab(generics.RetrieveUpdateDestroyAPIView):	
	serializer_class = CabSerializer
	queryset = Cab.objects.all()

class BookCab(APIView):
	def post(self, request):
		serializer = BookingSerializer(data=request.data)
		if serializer.is_valid():
			cab = serializer.validated_data['cab']
			if cab.is_booked:
				return Response({"message" : "The cab is already booked"}, status=status.HTTP_400_BAD_REQUEST)

			serializer.save()
			cab.is_booked = True
			cab.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

class ViewHistory(APIView):
	def get(self, request, *args, **kwargs):
		pk = self.kwargs['pk']
		try:
			user = User.objects.get(pk=pk)
		except User.DoesNotExist:
			return Response(status=status.HTTP_400_BAD_REQUEST)

		if user.is_driver:
			cab = Cab.objects.get(driver=user)
			queryset = Booking.objects.filter(cab=cab)
			serializer = BookingSerializer(queryset, many=True)
			return Response(serializer.data, status=status.HTTP_200_OK)		

		queryset = Booking.objects.filter(user=user)	
		serializer = BookingSerializer(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)			