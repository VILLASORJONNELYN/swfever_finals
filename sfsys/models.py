from django.db import models

class UserInfo(models.Model):
	surname = models.CharField(max_length = 200)
	firstname = models.CharField(max_length = 200)
	middleInitial = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	date = models.DateField(auto_now_add = True)
	region = models.TextField()

class PigInfo(models.Model):
	user_Info = models.ForeignKey("UserInfo", on_delete = models.CASCADE)
	date = models.CharField(max_length = 200)
	oth_symptoms = models.CharField(max_length = 200)
	Num_OtherSymp = models.IntegerField()
	Symptoms = models.CharField(max_length = 200)
	
class DeathRecords (models.Model):
	Region = models.CharField(max_length = 200)
	Date = models.CharField(max_length = 200)
	Num_Deaths = models.IntegerField()

	
