from django.contrib import admin
from .models import Booking,City

admin.site.register(Booking)
admin.site.register(City)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pickup_address', 'delivery_address', 'status', 'booking_date')
    list_filter = ('status', 'booking_date')
    search_fields = ('pickup_address', 'delivery_address', 'goods_type', 'user__username')

