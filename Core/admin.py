from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import Server

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('name',)

class ServerAdmin(admin.ModelAdmin):
	list_display = ('sv_id', 'active')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Server, ServerAdmin)