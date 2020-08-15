from django.urls import path
from . import views

# Computer Ｒeservation System (CRS)
app_name = 'crs'

urlpatterns = [
	path('test', views.test, name='test'),
	path('week/', views.WeekCalendar.as_view(), name='week'),
    path('week/<int:year>/<int:month>/<int:day>/', views.WeekCalendar.as_view(), name='week'),
]
