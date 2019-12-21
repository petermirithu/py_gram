from django.shortcuts import render,redirect
from django.contrib.auth import logout
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

def profile(request):
  '''
  view function that renders profile page
  '''
  title="Profile"
  return render(request,'profile.html',{"title":title})



