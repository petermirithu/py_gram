from django import forms
from .models import UserProfile,ImagePost,Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UpdateProfileForm(forms.ModelForm):
  '''
  class that defines how the update profile form will look like
  '''
  class Meta:    
    model=UserProfile
    exclude=['user','followers']

class UserUpdateForm(forms.ModelForm):
  '''
  class that defines how the update user form will look like
  '''
  class Meta:
    model=User
    fields=['username','email']

class ImagePostForm(forms.ModelForm):
  '''
  class that defines how the post form shall look like
  '''
  class Meta:
    model=ImagePost
    exclude=['posted_on','posted_by','likes']
class ImageCommentForm(forms.ModelForm):
  '''
  class that defines how the comment form shall look like
  '''
  class Meta:
    model=Comments
    exclude=['posted_on','image_id','posted_by']

class SignupForm(UserCreationForm):
  email = forms.EmailField(max_length=200, help_text='Required')
  class Meta:
      model = User
      fields = ('username', 'email', 'password1', 'password2')


  

