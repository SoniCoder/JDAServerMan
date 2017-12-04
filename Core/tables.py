import django_tables2 as tables
from .models import Customer
from django_tables2.export.views import ExportMixin


from .models import Customer




class CustomerTable(tables.Table):
    class Meta:
        model = Customer
        template = 'django_tables2/bootstrap.html'
        
class TableView(ExportMixin, tables.SingleTableView):
    table_class = CustomerTable
    model = Customer
    template_name = 'django_tables2/bootstrap.html'
        
           



