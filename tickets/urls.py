
from django.urls import path
from .views import *

urlpatterns=[
path('tickets/',tickets),
path('classify/',classify_api),
path('stats/',stats),
path('tickets/<int:id>/',update_status)
]
