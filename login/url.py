from django.conf.urls import url
from . import views

urlpatters = [
	url(r'^$', views.user_id, name='user_id'),
]