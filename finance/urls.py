from django.urls import path
from .views import *
from .models import *

app_name = 'finance'

urlpatterns = [
    path('', result, name='result'),
    path('predict/', predict.as_view(), name='predict'),
    path('apple_list/', ListView.as_view(), name='apple_list'),
]