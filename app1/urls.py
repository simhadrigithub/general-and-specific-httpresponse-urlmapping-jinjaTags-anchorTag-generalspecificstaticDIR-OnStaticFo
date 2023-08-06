from django.urls import path
from app1.views import *
app_name='app1'

urlpatterns =[
    path('nature/',nature,name='nature'),
    path('fruits/',fruits,name='fruits'),
    path('bigvalue/',bigvalue,name='bigvalue'),
]