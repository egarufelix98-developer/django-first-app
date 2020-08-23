from django.urls import path
from .views import(
	index)


app_name = "my_application"

urlpatterns = [
    path('',index,name='index'),
]
