from django.urls import path
from . import views


app_name = 'mainhome'


urlpatterns = [
    path('', views.index, name='index'),
    path('select/', views.select, name='select')
    
]