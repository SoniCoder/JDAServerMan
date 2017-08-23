from django.db import models

# Create your models here.


class Customer(models.Model):
	name = models.CharField(max_length=1000)
	#servers = models.ManyToManyField("Server", blank = True)
	SCPO =models.CharField(max_length=1000,blank=True, null=True)
	Versions=models.CharField(max_length=1000,blank=True, null=True)
	Citris_URL= models.CharField(max_length=1000,blank=True, null=True)
	FS_URL= models.CharField(max_length=1000,blank=True, null=True)
	JCES_URL =models.CharField(max_length=1000,blank=True, null=True)
	L3= models.CharField(max_length=1000,blank=True, null=True)
	PM = models.CharField(max_length=1000,blank=True, null=True)
	CDM= models.CharField(max_length=1000,blank=True, null=True)
	DB_SERVER=models.CharField(max_length=1000,blank=True, null=True)
	APPL_SERVER=models.CharField(max_length=1000,blank=True, null=True)
	SRE_SERVER= models.CharField(max_length=1000,blank=True, null=True)
	DB_Username=models.CharField(max_length=1000,blank=True, null=True)
	DB_Password=  models.CharField(max_length=1000,blank=True, null=True)
	Weblogic_Console=models.CharField(max_length=1000,blank=True, null=True)
	Weblogic_Password=models.CharField(max_length=1000,blank=True, null=True)
	
	def __str__(self):
		return self.name

class Server(models.Model):
	sv_id = models.CharField(max_length=1000)
	active = models.BooleanField(default=False)
	customer = models.ForeignKey(Customer, null=True)
	def __str__(self):
		return self.sv_id
