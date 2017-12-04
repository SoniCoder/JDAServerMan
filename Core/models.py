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

	def summarise(self):
		s = ",".join([str(self.name), str(self.Status), str(self.Product)])
		return s

        
        
class Server(models.Model):
	sv_id = models.CharField(max_length=1000)
	active = models.BooleanField(default=False)
	customer = models.ForeignKey(Customer, null=True)
	def __str__(self):
		return self.sv_id
