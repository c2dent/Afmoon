# -*- coding: utf-8 -*
from __future__ import unicode_literals
import mptt, uuid
from django.db import models
import base64
from mptt.models import MPTTModel, TreeForeignKey,TreeManyToManyField
import os
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from phone_login.models import User



class Region(MPTTModel):
	name = models.CharField(max_length=50, unique=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	class MPTTMeta:
		order_insertion_by = ['name']
		ordering = ('tree_id','level')

class CustomUser(User):
	region = TreeManyToManyField(Region, blank=True, related_name='user_region')
	jwt_secret = models.UUIDField(default=uuid.uuid4)
	def __str__(self):
		return self.phone_number

	def __unicode__(self):
		return self.phone_number

class Category(MPTTModel):
	name = models.CharField(max_length=50, unique=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='child', on_delete=models.CASCADE)

	def __str__(self):
		return self.name


	class MPTTMeta:
		order_insertion_by = ['name']
		ordering = ('tree_id','level')
		level_attr = 'mptt_level'

mptt.register(Region ,order_insertion_by=['name'])
mptt.register(Category,order_insertion_by=['name'])

class File(models.Model):
	file = models.FileField(blank=False, null=False)
	remark = models.CharField(max_length=20)
	timestamp = models.DateTimeField(auto_now_add=True)


class Ad(models.Model):
	title = models.CharField(max_length=30 , help_text='Title ads' , db_column='data')
	date_create = models.DateTimeField(auto_now=True,help_text='Date Create')
	description = models.TextField(max_length=300)
	region = TreeManyToManyField(Region, blank=True ,  related_name='reg')
	category = TreeManyToManyField(Category,blank=True ,  related_name='ad')
	views = models.IntegerField(blank=True, null=True)
	price = models.IntegerField(blank=True, null=True)
	phone_number = PhoneNumberField(blank=True)
	user = models.ForeignKey(CustomUser, related_name='ads', on_delete=models.CASCADE, blank=True, null=True)
	is_active = models.BooleanField(default=True)


	def __str__(self):
		return self.title

	@classmethod
	def create_ad(self,title, description, price, region, category, user):
		try:
			add_ad = Ad(title= title, description = description, price= price, user= user)
			add_ad.save()
			for cat in category:
				add_ad.category.add(cat)

			for reg in region:
				add_ad.region.add(reg)
				
			return add_ad
		except Exception as e:
			raise


class Image(models.Model):
	ad = models.ForeignKey(Ad, on_delete=models.CASCADE,blank=True,null=True, related_name='images')
	image = models.ImageField(blank=True, null=True, upload_to='images')

	def __str__(self):
		return self.image.name

	@classmethod
	def create_image(self, image):
		try:
			add_image = Image(image = image)
			add_image.save()
			
			return add_image
		except Exception as e:
			raise

def jwt_get_secret_key(user_model):
	return user_model.jwt_secret

# Create your models here.
