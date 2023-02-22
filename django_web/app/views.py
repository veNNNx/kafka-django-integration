from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import *
# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'sign_up.html', {'form': form})


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


@login_required(login_url='home.html')
def my_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        data = request.POST
        if data.get('email') != '':
            user = User.objects.get(id=request.user.id)
            user.email = data.get('email')
            user.save()

        profile.tel = data.get('tel') if data.get('tel') != '' else profile.tel
        profile.city = data.get('city') if data.get(
            'city') != '' else profile.city
        profile.zip_code = data.get('zip_code') if data.get(
            'zip_code') != '' else profile.zip_code
        profile.street = data.get('street') if data.get(
            'street') != '' else profile.street
        profile.addr_number = data.get('addr_number')
        profile.save()
        # messages.success(request, 'Profile updated!')
        return redirect('/my-profile')
    return render(request, 'my-profile.html', {'profile': profile})
