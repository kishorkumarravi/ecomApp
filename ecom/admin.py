from django.contrib import admin
# Register your models here.

from ecom.models import Registration2, Items, OrderHistory

admin.site.register(Registration2)
admin.site.register(Items)
admin.site.register(OrderHistory)