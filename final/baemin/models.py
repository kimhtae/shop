from django.db import models
from django.conf import settings

# Create your models here.

class Shop(models.Model):
	name = models.CharField(max_length=100)
	name_location = models.CharField(max_length=100)
	name_kr = models.CharField(max_length=100)
	tel = models.CharField(max_length=20)
	addr = models.CharField(max_length=100)
	# 정렬
	class Meta:
		ordering = ('-id',)
		
	def __str__(self):
		return self.name
		
class Item(models.Model):
	shop = models.ForeignKey('Shop', on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	name_type = models.CharField(max_length=100)
	price = models.PositiveIntegerField()
	# 정렬
	class Meta:
		ordering = ('-id',)	
		
	def __str__(self):
		return self.name

		
class Order(models.Model):
	shop = models.ForeignKey('Shop', on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	item_set = models.ManyToManyField(Item)
	created_at = models.DateTimeField(auto_now_add=True)
	
	# 정렬
	class Meta:
		ordering = ('-id',)
		
	@property
	def total(self):
		return sum(item.price for item in self.item_set.all())