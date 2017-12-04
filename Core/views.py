from django.shortcuts import render
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from .models import Customer
from .tables import CustomerTable
from .tables import TableView
from django_tables2.export.export import TableExport





def user_profile(request):
    custom=Customer.objects.all()
    table= CustomerTable(Customer.objects.all())
    RequestConfig(request,paginate={'per_page':15}).configure(table)
    
    return render(request, 'home.html', {'table': table,'custom':custom})
    

def TableView(request):
    table = CustomerTable(Customer.objects.all())

    RequestConfig(request).configure(table)

    export_format = request.GET.get('_export', None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response('table.{}'.format(export_format))

    return render(request, 'table.html', {
        'table': table
    })


def MyView(request):
    
    query_results = Customer.objects.all()
    
    return render_to_response(request,'home.html',{'query_results':query_results})

                  
                  


# Create your views here.las
