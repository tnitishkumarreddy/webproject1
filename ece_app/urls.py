from ece_app.views import *
from django.urls import path

app_name='my'

urlpatterns=[
    path('ecedept/',ecedept,name='ecedept'),
    path('ecestudents/',ecestudents,name='ecestudents'),
]