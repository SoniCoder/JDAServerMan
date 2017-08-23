from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import Server

class ServersInline(admin.TabularInline):
   model = Server

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('name',)
	inlines = [
        ServersInline,
	]
	#exclude = ('servers',)
class ServerAdmin(admin.ModelAdmin):
	list_display = ('sv_id', 'active')
	list_filter = ('customer',)
	# inlines = [
        # ServersInline,
	# ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Server, ServerAdmin)
