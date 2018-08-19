# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework.decorators import detail_route,list_route
from .models import (Ad,User,Category,Region, CustomUser,Image)
from trans import trans
from .serializers import (AdSerializer,CategorySerializer,
	RegionSerializer, AdRegionSerializer, CustomUserSerializer,
	 AdCreateSerializer, ImageSerializer, Base64ImageField, FileSerializer, ProfileSerializer,
	 AdGetSerializer)
from rest_framework import generics
from django.shortcuts import render
import uuid
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, permission_classes


class CreateAd(viewsets.ModelViewSet):
	permission_classes = (AllowAny,)
	serializer_class = AdSerializer
	queryset = Ad.objects.all()

	def create(self, request, format=None):
		categoryId = request.data.get('categoryId', None)
		regionId = request.data.get('regionId',None)
		category = []
		region = []
		for cat in categoryId:
			category.append(Category.objects.get(id = int(cat)))

		for reg in regionId:
			region.append(Region.objects.get(id = int(reg)))

		userId = int(request.data.get('userId',None))
		user = CustomUser.objects.get(id = userId)
		title = request.data.get('title')
		description = request.data.get('description')
		price = request.data.get('price')

		try:
			ad = Ad.create_ad(title, description,price,region,category,user)
			if request.data.get('images'):
				for img in request.data.get('images'):
					img_token = {
					'image': img,
					'ad': ad.id
					}
					ser = ImageSerializer(data = img_token)
					if ser.is_valid():
						ser.save()
			if  ad :
				serializer = self.serializer_class(ad)
				return Response(serializer.data)
			return Response({
				'reason': "you can not have more than {n} attempts per day, please try again tomorrow".format(
					n=getattr(settings, 'PHONE_LOGIN_ATTEMPTS', 10))}, status=status.HTTP_403_FORBIDDEN)
		except Exception as e:
			raise

# class UserLogoutView(views.APIView):
# 	permission_classes = (IsAuthenticated)
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def UserLogout(request, *args, **kwargs):
	user = request.user
	user.jwt_secret = uuid.uuid4()
	user.save()
	return Response(status=status.HTTP_204_NO_CONTENT)

class ProfileViewSet(viewsets.ViewSet):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	serializers_class = ProfileSerializer

	def list(self, request):
		user = request.user
		serializer = ProfileSerializer(user)
		return Response(serializer.data)

class AdfilterViewSet(viewsets.ViewSet):
	permission_classes = (AllowAny,)
	serializers_class = AdGetSerializer
	def list(self, request, region=None, category=None):
		queryset = Ad.objects.all()
		self.regionId = CheckRegion(region)
		queryset = queryset.filter(region=self.regionId)
		self.categoryId = CheckCategory(category)
		queryset = queryset.filter(category=self.categoryId)
		serializers = AdGetSerializer(queryset, many=True)
		return Response(serializers.data)


	def retrieve(self, request, region=None, category=None, pk=None):
		self.regionId = CheckRegion(region)
		queryset = Ad.objects.filter(is_active=True)
		queryset =Ad.objects.filter(region = self.regionId)
		self.categoryId = CheckCategory(category)
		queryset =Ad.objects.filter(category= self.categoryId)
		param = get_object_or_404(queryset, pk=pk)
		serializers = AdGetSerializer(param)
		return Response(serializers.data)

	def destroy(self, request ,region=None, category=None, pk= None):

		instance = self.get_object(pk).delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def get_object(self, id):
		ad = Ad.objects.get(id = id)
		return ad


class RegionfilterViewSet(viewsets.ViewSet):
	permission_classes = (AllowAny,)
	def list(self, request, region=None):
		queryset = Ad.objects.all()
		self.regionId = CheckRegion(region)
		queryset = queryset.filter(region= self.regionId)
		serializers = AdGetSerializer(queryset, many=True)
		return Response(serializers.data)

class TestViewSet(viewsets.ViewSet):
	permission_classes = (AllowAny,)
	def list(self, request, region=None):
		queryset = Ad.objects.all()
		serializers = AdSerializer(queryset, many=True)
		return Response(serializers.data)

class CustomUserViewSet(viewsets.ViewSet):
	permission_classes = (AllowAny,)
	def list(self, request):
		queryset = CustomUser.objects.all()
		serializers = CustomUserSerializer(queryset, many=True)
		return Response(serializers.data)

	def retrieve(self, request, pk=None):
		queryset = CustomUser.objects.all()
		param = get_object_or_404(queryset, pk=pk)
		serializers = CustomUserSerializer(param)
		return Response(serializers.data)

class ImageViewSet(viewsets.ModelViewSet):
	permission_classes = (AllowAny,)
	queryset = Image.objects.all()
	serializer_class = ImageSerializer



def CheckRegion(region):
	regions = Region.objects.all()
	for reg in regions:
		if (region.lower() == trans(reg.name, 'slug').lower()):
			return reg.id
			break

def CheckCategory(category):
	categoryes = Category.objects.all()
	for categor in categoryes:
		if (category).lower() == (trans(categor.name, 'slug')).lower():
			return categor.id
		else: 
			return None


# Create your views here.
