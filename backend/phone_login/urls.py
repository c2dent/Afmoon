from django.conf.urls import url

from .views import GenerateOTP, Registration, authenticate_user, ChangePasswordView

urlpatterns = [
    url(r'^generate/$', GenerateOTP.as_view(), name="generate"),
    url(r'^changepsw/$', ChangePasswordView.as_view(), name='new_password'),
    url(r'^registration/$', Registration.as_view(), name="registration"),
    url(r'^login/$', authenticate_user),
]