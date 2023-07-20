from django.db import models

#class UserProfile(models.Model):
#	name=models.CharField(max_length=20)
#	age=models.CharField(max_length=10)
#	gender=models.CharField(max_length=10)
#	email=models.EmailField()


class Userprofile(models.Model):
	name=models.CharField(max_length=20)
	age=models.IntegerField()
	gender=models.CharField(max_length=10)
	email=models.EmailField()
# Create your models here.

class Address_details(models.Model):
	pin_code=models.IntegerField()
	address=models.TextField(max_length=50)
	user=models.ForeignKey(Userprofile,on_delete=models.CASCADE)