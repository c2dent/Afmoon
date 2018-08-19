from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import  (AdfilterViewSet, RegionfilterViewSet,TestViewSet, CustomUserViewSet, CreateAd, 
	ImageViewSet, UserLogout, ProfileViewSet)
from django.conf.urls import url
from rest_framework_nested import routers
from django.conf.urls import include
from django.contrib import admin
from rest_framework_jwt import views as jwt_views
from phone_login.views import ChangePasswordView

router = routers.SimpleRouter()
router.register(r'aditem', CreateAd, base_name='ad')
router.register(r'profile' , ProfileViewSet, base_name='profile')
router.register(r'users', CustomUserViewSet, base_name='ads')
router.register(r'(?P<region>[^/.]+)', RegionfilterViewSet, base_name='ads')
router.register(r'(?P<region>[^/.]+)/(?P<category>[^/.]+)' , AdfilterViewSet, base_name='ads')

urlpatterns = [
	url(r'profile/logout' , UserLogout),
	url(r'^profile/changepsw/$', ChangePasswordView, name='new_password'),
	url(r'^phone_login/', include(('phone_login.urls', 'phone_login'), namespace='phone_login'),),
	url(r'^admin/', admin.site.urls),
	url(r'^accounts/', include('django.contrib.auth.urls')),
	url(r'^', include(router.urls)),
	url(r'^test/', TestViewSet.as_view({'get': 'list'})),
	]