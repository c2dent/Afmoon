# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Ad,Region,Category,Image
from mptt.admin import MPTTModelAdmin

# class AdAdmin(admin.ModelAdmin):
# 	fields = ['title','description','price','phone_number','is_active','category', 'region','user']

class RegionAdmin(admin.ModelAdmin):
	fields = ['parent', 'name']

class CategoryAdmin(admin.ModelAdmin):
	fields = ['parent', 'name']

class PictureAdmin(admin.ModelAdmin):
	fields = ['image']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(Ad)
admin.site.register(Image)
# Register your models here.
