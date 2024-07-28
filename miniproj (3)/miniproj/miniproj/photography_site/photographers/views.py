from django.shortcuts import render, redirect, get_object_or_404
from .models import Photographer,Booking
from .forms import PhotographerForm, BookingForm
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from datetime import datetime
from photographers.models import Contact,Cuslogin
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'authenticate/home.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully')
            return redirect('photographers_list')
        else:
            messages.warning(request, "Username or Password is incorrect !!")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')
    

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            form = SignUpForm(request.POST)
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'authenticate/register.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('photographers_list')
    else:
        form = EditProfileForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'authenticate/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Changed Successfully")
            return redirect('home')
    else:
        form = ChangePasswordForm(user=request.user)
        print(form)
    context = {
        'form': form,
    }
    return render(request, 'authenticate/change_password.html', context)

















def index(request):
    return render(request,'index.html')
def cuslogin(request):
    return render(request,'cuslogin.html')
def about(request):
    return render(request, 'about.html')

def photographer_register(request):
    if request.method == 'POST':
        form = PhotographerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photographers_list')
    else:
        form = PhotographerForm()
    return render(request, 'photographers/photographer_register.html', {'form': form})

def photographers_list(request):
    photographers = Photographer.objects.all()
    return render(request, 'photographers/photographers_list.html', {'photographers': photographers})

def photographer_detail(request, pk):
    photographer = get_object_or_404(Photographer, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('photographer_detail', pk=pk)
    else:
        form = BookingForm(initial={'photographer': photographer})
    return render(request, 'photographers/photographer_detail.html', {'photographer': photographer, 'form': form})
def photographer_bookings(request, pk):
    photographer = get_object_or_404(Photographer, pk=pk)
    bookings = Booking.objects.filter(photographer=photographer)
    return render(request, 'photographers/photographer_bookings.html', {'photographer': photographer, 'bookings': bookings})

def cuslogin(request):
    if request.method=="POST":
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        #mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        #address=request.POST.get('address')
        #city=request.POST.get('city')
        cuslogin=Cuslogin(fullname=fullname,email=email,password=password)
        cuslogin.save()
    return render(request,'cuslogin.html')



def contact(request):
    if request.method=="POST":
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        contact=request.POST.get('contact')
        contact=Contact(fullname=fullname,email=email,mobile=mobile,contact=contact,date=datetime.today())
        contact.save()
    return render(request,'contact.html')

def photographer1(request):
     if request.method=="POST":
        fullname=request.POST.get('fullname')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        password=request.POST.get('password')
        address=request.POST.get('address')
        city=request.POST.get('city')
        yourworks=request.POST.get('yourworks')
        photographer1=Photographer(fullname=fullname,mobile=mobile,email=email,password=password,address=address,city=city,yourworks=yourworks)
        photographer1.save()
     return render(request,'photographer1.html')


