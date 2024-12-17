from cse_app.views import *
from django.urls import path

app_name='other'

urlpatterns=[
    path('csedept/',csedept,name='csedept'),
    path('csestudents/',csestudents,name='csestudents'),
]