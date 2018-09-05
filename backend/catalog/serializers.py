import re
import base64
import uuid
import imghdr
from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Ad,User,Image, Category,Region,CustomUser, File

class Base64ImageField(serializers.ImageField):
	def to_internal_value(self, data):
		from django.core.files.base import ContentFile
		import base64
		import six
		import uuid

		if isinstance(data, six.string_types):
			if 'data:' in data and ';base64,' in data:
				header, data = data.split(';base64,')
			try:
				decoded_file = base64.b64decode(data)
			except TypeError:
				self.fail('invalid_image')

			file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
			file_extension = self.get_file_extension(file_name, decoded_file)

			complete_file_name = "%s.%s" % (file_name, file_extension, )

			data = ContentFile(decoded_file, name=complete_file_name)

		return super(Base64ImageField, self).to_internal_value(data)
		
	def get_file_extension(self, file_name, decoded_file):
		import imghdr

		extension = imghdr.what(file_name, decoded_file)
		extension = "jpg" if extension == "jpeg" else extension
		return extension

class ImageSerializer(serializers.ModelSerializer):
	image = Base64ImageField(max_length=None, use_url=True,)
	
	class Meta:
		model = Image
		fields = ('image','ad')



class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('id','nickname', 'phone_number', 'password')

	def create(self, validated_data):
		user = super(CustomUserSerializer, self).create(validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user

class AdUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('id','nickname', 'phone_number')

class AdSerializer(serializers.ModelSerializer):
	# images = serializers.StringRelatedField(many = True)
	images = ImageSerializer(many = True)
	user = AdUserSerializer()
	class Meta:
		model = Ad
		fields = ('title', 'description', 'region', 'category','price' , 'date_create','id','views','phone_number', 'is_active','user', 'images')

class AdGetSerializer(serializers.ModelSerializer):
	images = serializers.StringRelatedField(many = True)
	user = AdUserSerializer()
	class Meta:
		model = Ad
		fields = ('title', 'description', 'region', 'category','price' , 'date_create','id','views','phone_number', 'is_active','user', 'images')


class CategorySerializer(serializers.ModelSerializer):
	# ad = AdSerializer(many=True)
	# child = RecursiveField(allow_null=True,required=False,many=True)
	class Meta:
		model = Category
		# fields = ('name','id','ad','child','lft','rght')
		fields = ('name','id')
	
class RegionSerializer(serializers.ModelSerializer):
	# children = RecursiveField(allow_null=True, required=False,many=True)

	class Meta:
		model = Region
		fields = ('name','id')

class AdRegionSerializer(serializers.ModelSerializer):
	children = RecursiveField(allow_null=True,required=False,many=True)
	reg = AdSerializer(many=True)
	class Meta:
		model = Region
		fields = ('children','reg','id','name')

class AdCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model= Ad
		fields = ('title','description', 'price', 'category', 'region', 'user')

class ProfileSerializer(serializers.ModelSerializer):
	ads = AdSerializer(many=True)

	class Meta:
		model = CustomUser
		fields = ('nickname', 'avatar', 'ads', 'region', 'phone_number')