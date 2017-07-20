from django.db import models

# Create your models here.
class Server(models.Model):
	sv_id = models.CharField(max_length=250)
	active = models.BooleanField(default=False)
	
	def __str__(self):
		return self.sv_id


class Customer(models.Model):
	name = models.CharField(max_length=250)
	servers = models.ManyToManyField("Server")
	
	def __str__(self):
		return self.name