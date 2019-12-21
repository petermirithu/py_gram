from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from PIL import Image 

# Create your models here.
class UserProfile(models.Model):
  '''
  class that defines how the profile data os a user will be stored in the database
  '''
  user=models.OneToOneField(User, on_delete=models.CASCADE)
  status=models.CharField(max_length=1000,blank=True)  
  pic=ImageField(blank=True,manual_crop='')
  career=models.CharField( max_length=100,blank=True)

  def __str__(self):
    return self.user.username  




