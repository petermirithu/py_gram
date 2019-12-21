from django import forms
from .models import UserProfile
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
    


  

