from django.conf.urls import url, include
from . import views


urlpatterns = [
	#homepage
	url(r'^$', views.index, name='index'),
	url(r'^contact/', views.contact, name='contact'),
]
