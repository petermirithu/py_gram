from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import UserProfile,ImagePost,Comments
from .forms import UpdateProfileForm,UserUpdateForm,ImagePostForm,ImageCommentForm,SignupForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .email import send_welcome_email


def home(request):
  '''
  view function that renders the home page
  '''
  posts=ImagePost.get_images_all()
  return render(request,'index.html',{"posts":posts})
  
@login_required(login_url="/accounts/login/")
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
  posts=ImagePost.get_user_posts(request.user.id)    
  return render(request,'profile.html',{"title":title,"posts":posts})

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
  comments=Comments.get_post_comments(imageId)
      
  return render(request,'single_post.html',{"form":form,"comments":comments,"post":image_posted})      

@login_required(login_url="/accounts/login/")
def like_post(request):
  '''
  function that add a user to like field when he/she likes a post
  '''
  post=get_object_or_404(ImagePost, id=request.POST.get('post_id'))  
  post.likes.add(request.user)      
  return redirect('Home')

@login_required(login_url="/accounts/login/")
def follow_user(request):
  '''
  function that adds a user to follow field when he/she followers another user
  '''
  follow=get_object_or_404(UserProfile,id=request.POST.get('user_id'))
  follow.followers.add(request.user)  
  return redirect('Home')

@login_required(login_url="/accounts/login/")
def others_profile(request, username):
  '''
  view function that renders other users profile page
  '''
  other_user=User.objects.get(username=username)
  title=other_user.username
  posts=ImagePost.get_user_posts(other_user.id)       
  return render(request,'others_profile.html',{"title":title,"posts":posts,"other_user":other_user}) 

@login_required(login_url="/accounts/login/")
def search(request):
  '''
  view function that render search template with results  
  '''
  if 'search_term' in request.GET and request.GET["search_term"]:

    search_term=request.GET.get('search_term')
    try:
      posts_by_name=ImagePost.get_posts_by_name(search_term)
      message=f'{search_term}'
      title="Searched"

      if posts_by_name:  
        return render(request, 'search.html',{"posts":posts_by_name,"title":title,"message":message})
    except ObjectDoesNotExist:        
      message=f'{search_term}'
      title="Searched"
      return render(request, 'search.html',{"title":title,"message":message})

    try:
      found_user=User.objects.get(username=search_term)      
      user_posts=ImagePost.get_user_posts(found_user.id)
      print('******************************')
      print(found_user.username)
      print('******************************')
      message=f'{search_term}'
      title="Searched"
      if user_posts or follow_user:                                        
        return render(request, 'search.html',{"user_f":found_user,"posts":user_posts,"title":title,"message":message})
    except ObjectDoesNotExist:
      message=f'{search_term}'
      title="Searched"
      return render(request, 'search.html',{"title":title,"message":message})   

def signup(request):
  '''
  view function to send emails to new users when they register
  '''
  if request.method=='POST':
    form=SignupForm(request.POST)
    if form.is_valid():
      form.save()
      name=form.cleaned_data['username']
      email=form.cleaned_data['email']      
      send_welcome_email(name,email)
      HttpResponseRedirect('Home')

  else:
    form=SignupForm()

  return render(request,'registration/registration_form.html',{"form":form})        




