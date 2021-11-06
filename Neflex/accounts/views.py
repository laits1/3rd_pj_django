from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
import requests
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from .forms import CustomCreationForm
from django.contrib import auth


# Create your views here.
def login(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None : 
            auth.login(request, user)
            # if user.like_movie:
                # return redirect('main:index')
            return redirect('/select')
        else :
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else :
        return render(request, 'accounts/login.html')


def logout(request) :
    auth.logout(request)
    return redirect('accounts:login')

def home(request) :
    return render(request, 'accounts/login.html')


def signup(request) :
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        context={'form':form}
        return render(request, 'accounts/login.html')
        #유저 정보 저장
	
        # id = request.POST.get('name')
        # password = request.POST.get('password')

        # hashed_password = make_password(password)

        # get_user_model().objects.create(
        #     username=id,
        #     password=hashed_password)
        # return redirect('accounts:login')


    else:
        form = CustomCreationForm()

        context = {
            'form': form,
        }

        return render(request, 'accounts/signup.html', context)