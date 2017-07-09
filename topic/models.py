from django.db import models
from datetime import datetime

class PersonDetails(models.Model):
	name=models.CharField(max_length=250)
	profession=models.CharField(max_length=500)
	age=models.IntegerField()
	
	def __str__(self):
		return self.name

class Blogs(models.Model):		
	author=models.ForeignKey(PersonDetails,on_delete=models.CASCADE)
	title=models.CharField(max_length=500)
	time=models.DateTimeField(default=datetime.now,blank=True)
	content=models.CharField(max_length=20000)
	