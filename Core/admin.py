from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from .models import Customer
from .models import Server

#admin.site.disable_action('delete_selected')

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

class CustomerResource(resources.ModelResource):
   
   class Meta:
      model=Customer
      
class CustomerAdmin(ImportExportActionModelAdmin):
   pass



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Server, ServerAdmin)
