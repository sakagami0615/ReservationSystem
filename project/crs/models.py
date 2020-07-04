from django.db import models
from django.utils import timezone


class User(models.models):

	user_id = models.IntegerField(primary_key=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

	unlocker = models.BooleanField(default=False)

	department = models.CharField(
		blank=True,
		null=True,
		max_length=100)
	division = models.CharField(
		blank=True,
		null=True,
		max_length=100)
	team = models.CharField(
		blank=True,
		null=True,
		max_length=100)

	create_date = models.DateTimeField(auto_now_add = True)
	update_date = models.DateTimeField(auto_now = True)


class Plan(models.models):

	day = models.DateField()
	begin_time = models.TimeField()
	end_time = models.TimeField()
	
	create_date = models.DateTimeField(auto_now_add = True)
	update_date = models.DateTimeField(auto_now = True)

	user = models.ForeignKey(User, verbose_name='Plan', on_delete=models.CASCADE)