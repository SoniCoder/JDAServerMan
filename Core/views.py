from django.shortcuts import render
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from .models import Customer
from .tables import CustomerTable
from .tables import TableView

from django_tables2.export.export import TableExport





def user_profile(request):
    q = request.GET.get('q','')
    custom = Customer.objects.all()
    r= request.GET.get('rtext','')

    
    if (q and r=="Status"):
            custom=custom.filter(Status__contains=q)
     
    elif(q and r=="Customer Name"):   
        custom=custom.filter(name__contains=q)
            
    elif(q and r=="Product"):  
        custom=custom.filter(Product__contains=q)
          
    elif(q and r=="L3"):       
        custom=custom.filter(L3__contains=q)
    
    elif(q and r=="Server Type"):  
        custom=custom.filter(Server_Type__contains=q)
            
    elif(q and r=="Version"):  
        custom=custom.filter(Version__contains=q)
            
    elif(q and r=="PM"):  
        custom=custom.filter(PM__contains=q)
            
    elif(q and r=="CDM"):         
        custom=custom.filter(CDM__contains=q)
        
    
        
    

    import csv
    
     
        
    f = open("static/output.csv", "w")
   
    f.write("Customer Name" + "," + "Status" + "," + "Product" + "," + "Operating System" + "," +"Server_Type" + "," + "Version"+"," +"Citrux_URL"+"," +"F5_URL"+"," +"SSO"+"," +"SSO_URL"+"," +"JCES_URL"+","
            +"L3"+"," +"PM"+"," +"CDM"+"," +"DB_SERVER"+"," +"APPL_SERVER"+"," +"SRE_SERVER"+","+"DB_Username"+"," +"DB_Password"+"," +"Application Login"+","
            +"Application Password"+"," +"Weblogic Console"+"," +"Weblogic password"+"," +"Cluster"+"," +"Sharepoint Link"+"," +"SLA"+ "," +"Customer_DL" + "," + "Control M Template" +"\n")
        
    for c in custom:
        f.write(c.summarise()+"\n")
        
    #with open('output.csv','w') as csvfile:
        #writer = csv.writer(csvfile, delimiter='$', quoting=csv.QUOTE_MINIMAL)
        #for c in custom:
            #writer.writerow(c.summarise()+"\n")
        

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
