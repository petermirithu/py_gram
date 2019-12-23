from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import UserProfile,ImagePost,Comments
from .forms import UpdateProfileForm,UserUpdateForm,ImagePostForm,ImageCommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponseRedirect,HttpResponse
def home(request):
  '''
  view function that renders the home page
  '''
  posts=ImagePost.get_images_all()
  return render(request,'index.html',{"posts":posts})

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
  view function that renders the update profile form
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

@login_required(login_url="/accounts/login/")
def new_post(request):
  '''
  view function that renders a form for creating a new post
  '''  
  if request.method=='POST':
    form=ImagePostForm(request.POST,request.FILES)
    if form.is_valid():
      post=form.save(commit=False)
      post.posted_by=request.user
      post.save()

      return redirect('Home')
  else:
    form=ImagePostForm()    

  return render(request,'new_post.html',{"form":form})  

@login_required(login_url="/accounts/login/")
def single_post(request, id):
  '''
  view function that renders a single post and  comments sections
  '''  
  if request.method=='POST':
    form=ImageCommentForm(request.POST)
    if form.is_valid():
      comment=form.save(commit=False)
      comment.posted_by=request.user      
      post=ImagePost.objects.get(id=id)
      comment.image_id=post
      comment.save()
      HttpResponseRedirect('single_post')
  else:
    form=ImageCommentForm()

  image_posted=ImagePost.single_image(id)  
  imageId=ImagePost.get_image_id(id)
  comments=Comments.get_user_comments(imageId)
      
  return render(request,'single_post.html',{"form":form,"comments":comments,"post":image_posted})      



