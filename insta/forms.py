from django import forms
from .models import UserProfile,ImagePost,Comments
from django.contrib.auth.models import User

class UpdateProfileForm(forms.ModelForm):
  '''
  class that defines how the update profile form will look like
  '''
  class Meta:    
    model=UserProfile
    exclude=['user']

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
    exclude=['posted_on','posted_by']
class ImageCommentForm(forms.ModelForm):
  '''
  class that defines how the comment form shall look like
  '''
  class Meta:
    model=Comments
    exclude=['posted_on','image_id','posted_by']




  

