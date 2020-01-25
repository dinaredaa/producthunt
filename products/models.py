from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
	title = models.CharField(max_length=255, null=True)
	pub_date = models.DateField(blank=True, null=True)
	body = models.TextField(null=True)
	url = models.TextField(null=True)
	icon = models.ImageField(upload_to='images/', null=True)
	image = models.ImageField(upload_to='images/', null=True)
	votes_total = models.IntegerField(default=1)
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def summery(self):
		return self.body[:100]

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %y')
