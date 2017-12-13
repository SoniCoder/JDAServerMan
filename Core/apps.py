from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'Core'

	# def ready(self):
	# 	pass
class CustomConfig(AppConfig):
	name ='Core'
	def ready(self):
		pass