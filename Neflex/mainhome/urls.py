from django.urls import path
from . import views


app_name = 'mainhome'


urlpatterns = [
    path('', views.home, name='home'),
    path('select/', views.select, name='select')
    
]