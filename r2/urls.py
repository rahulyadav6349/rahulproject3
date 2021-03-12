from django.urls import path
app_name='r2'
from r2 import views
urlpatterns=[
    path('ashu/',views.ashu,name='ashu'),
]