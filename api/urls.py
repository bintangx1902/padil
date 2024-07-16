from django.urls import path
from .views import *


urlpatterns = [
    path('', GetResult.as_view(), name='get-result')
]

