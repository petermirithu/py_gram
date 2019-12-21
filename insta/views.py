from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UpdateProfileForm,UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
  '''
  view function that renders the home page
  '''
  return render(request,'index.html')

def logout_request(request):
  '''
  view function renders home page once logout
  '''
  logout(request)
  return redirect('Home')

@login_required(login_url="/accounts/login/")
def profile(request):
  '''
  view function that renders profile page
  '''
  title="Profile"      
  return render(request,'profile.html',{"title":title})

@login_required(login_url="/accounts/login/")
def update_profile(request):
  '''
  view function that renders the updat profile form
  '''      
  if request.method=='POST':
    user_form=UserUpdateForm(request.POST, instance=request.user)
    profile_form=UpdateProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()            
      return redirect("profile")
  else:
    user_form=UserUpdateForm(instance=request.user)
    profile_form=UpdateProfileForm(instance=request.user.userprofile)

  context={
    'user_form':user_form,
    'profile_form':profile_form,
  }

  return render(request,'updateprofile.html',context)    




