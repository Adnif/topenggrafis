from django.contrib import admin

# Register your models here.
from order.models import Customer

admin.site.register(Customer)