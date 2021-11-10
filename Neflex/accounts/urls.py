from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('after_login_page/', views.after_login, name='after_login'),
    path('mood/', views.mood, name='mood'),
 




    path('moviepage/', views.moviepage, name='moviepage')
]