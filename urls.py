from django.urls import path
from .views import *
app_name='app2'

urlpatterns = [
    path('app2/home',Homepage,name='homepageurl'),
    path('app2/add/',addFood,name='addfoodurl'),
    path('app2/list/',foodlist,name='listfoodurl'),
]
