from django.urls import path
from . import views

# Computer Ｒeservation System (CRS)
app_name = 'crs'

urlpatterns = [
	path('', views.test, name='test')
]
