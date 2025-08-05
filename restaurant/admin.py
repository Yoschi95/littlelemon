from django.contrib import admin
from .models import Menu, Booking

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'Price', 'Inventory')  # Replace with your actual field names

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'BookingDate', 'No_of_guests')  # Replace with your actual field names

admin.site.register(Menu, MenuAdmin)
admin.site.register(Booking, BookingAdmin)