from django.contrib import admin
from .models import Cab, Booking, User

# Register your models here.
admin.site.register(Cab)
admin.site.register(Booking)
admin.site.register(User)