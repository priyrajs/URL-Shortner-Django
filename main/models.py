from django.db import models

# Create your models here.

class Url_details(models.Model):
	id = models.IntegerField(primary_key=True)
	input_url = models.CharField(max_length=300,unique=True)
	output_url = models.CharField(max_length=100,null=True)
