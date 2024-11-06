from django.urls import path
from . import views     
    
urlpatterns = [
    path('', views.index),
    path('addnew', views.addnew),
    # path('result', views.result),
]


