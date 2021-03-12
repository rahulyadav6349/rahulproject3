from django.urls import path
app_name='app1'
from app1 import views
urlpatterns=[
    path('rahul/',views.rahul,name='rahul  '),
]