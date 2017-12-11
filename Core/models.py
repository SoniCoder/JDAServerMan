from django.db import models

# Create your models here.


class Customer(models.Model):
	Choic=(
		    ('-','-'),
			('physical','Physical'),
			('vm','VM'),
			('lpar','LPAR'),
	)
	Choice=(
		('-','-'),
		('yes','Yes'),
		('no','No')
	)
	Option=(
		('Steady','Steady'),
		('Transition','Transitoion'),
		('Decomm','Decomm')
	)
	name = models.CharField(max_length=1000)
	Status =models.CharField(max_length=1000,choices=Option, null=True)
	#servers = models.ManyToManyField("Server", blank = True)
	Product =models.CharField(max_length=1000,blank=True, null=True)
	Operating_System=models.CharField(max_length=1000,blank=True, null= True)
	Server_Type=models.CharField(max_length=10, choices = Choic, default='-')
	Version=models.CharField(max_length=1000,blank=True, null=True)
	Citrux_URL= models.CharField(max_length=1000,blank=True, null=True)
	F5_URL= models.CharField(max_length=1000,blank=True, null=True)
	SSO=models.CharField(max_length=10, choices = Choice, default='-')
	SSO_URL= models.CharField(max_length=1000,blank=True, null=True)
	JCES_URL =models.CharField(max_length=1000,blank=True, null=True)
	L3= models.CharField(max_length=1000,blank=True, null=True)
	PM = models.CharField(max_length=1000,blank=True, null=True)
	CDM= models.CharField(max_length=1000,blank=True, null=True)
	DB_SERVER=models.CharField(max_length=1000,blank=True, null=True)
	APPL_SERVER=models.CharField(max_length=1000,blank=True, null=True)
	SRE_SERVER= models.CharField(max_length=1000,blank=True, null=True)
	DB_Username=models.CharField(max_length=1000,blank=True, null=True)
	DB_Password=  models.CharField(max_length=1000,blank=True, null=True)
	Application_Login=models.CharField(max_length=1200,blank=True, null=True)
	Application_Password=models.CharField(max_length=1200,blank=True, null=True)
	Weblogic_Console=models.CharField(max_length=1000,blank=True, null=True)
	Weblogic_Password=models.CharField(max_length=1000,blank=True, null=True)
	Cluster=models.CharField(max_length=10, choices = Choice, default='-')
	SharePoint_Link=models.CharField(max_length=1000,blank=True, null=True)
	SLA=models.CharField(max_length=1000,blank=True, null=True)
	P_and_P_Link=models.CharField(max_length=1000,blank=True, null=True)
	Customer_DL=models.CharField(max_length=1000,blank=True, null=True)
	Control_M_Template=models.CharField(max_length=1000,blank=True, null=True)
	
	
	
	def __str__(self):
		return self.name
	

	def abcd(self):
		r=",".join(["Customer Name", "Status" ,"Product" ,"Operating System" ,"Server_Type" ,"Version" ,"Citrux_URL" ,"F5_URL" ,"SSO" ,"SSO_URL" ,"JCES_URL" ,"L3" ,"PM" ,"CDM" ,"DB_SERVER" ,"APPL_SERVER" ,"SRE_SERVER"
					,"DB_Username" ,"DB_Password" ,"Application Login" ,"Application Password" ,"Weblogic Console" ,"Weblogic password" ,"Cluster" ,"Sharepoint Link" ,"SLA" ,"Customer_DL"  ,"Control M Template"])
		return r

	def summarise(self):
		s = ",".join([str(self.name), str(self.Status), str(self.Product),str(self.Operating_System),str(self.Server_Type),str(self.Version),str(self.Citrux_URL),
					  str(self.F5_URL),str(self.SSO),str(self.SSO_URL),str(self.JCES_URL),str(self.L3),str(self.PM),str(self.CDM),str(self.DB_SERVER),str(self.APPL_SERVER),
					  str(self.SRE_SERVER),str(self.DB_Username),str(self.DB_Password),str(self.Application_Login),str(self.Application_Password),str(self.Weblogic_Console),
					  str(self.Weblogic_Password),str(self.Cluster),str(self.SharePoint_Link),str(self.SLA),str(self.P_and_P_Link),str(self.Customer_DL),str(self.Control_M_Template)])
		return s

        
        
class Server(models.Model):
	sv_id = models.CharField(max_length=1000)
	active = models.BooleanField(default=False)
	customer = models.ForeignKey(Customer, null=True)
	def __str__(self):
		return self.sv_id
