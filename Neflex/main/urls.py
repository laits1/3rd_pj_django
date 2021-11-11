from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('select/', views.select, name='select'),
    path('moviepage/<int:movie_id>', views.moviepage, name='moviepage')
]

