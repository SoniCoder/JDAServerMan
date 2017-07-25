from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import Server

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_filter = ('servers',)
class ServerAdmin(admin.ModelAdmin):
	list_display = ('sv_id', 'active')
	list_filter=('customer',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Server, ServerAdmin)