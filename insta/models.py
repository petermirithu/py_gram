from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from tinymce.models import HTMLField
# Create your models here.
class UserProfile(models.Model):
  '''
  class that defines how the profile data os a user will be stored in the database
  '''
  user=models.OneToOneField(User, on_delete=models.CASCADE)
  status=models.CharField(max_length=1000,blank=True)  
  pic=ImageField(blank=True,manual_crop='')
  career=models.CharField( max_length=100,blank=True)
  followers=models.ManyToManyField(User, related_name="followers",blank=True)

  def __str__(self):
    return self.user.username  
  
  

  @classmethod
  def search_user(cls,username):    
    '''    
    function that searches for a user
    '''    
    found=User.objects.get(username=username)
    return found


class ImagePost(models.Model):
  '''
  class that defines how post details are to be stored in the database
  '''
  image=ImageField(blank=True,manual_crop='')
  image_name=models.CharField(max_length=50)
  caption=HTMLField()
  likes=models.ManyToManyField(User,related_name="likes",blank=True)
  posted_by=models.ForeignKey(User, on_delete=models.CASCADE)
  posted_on=models.DateField(auto_now_add=True)

  class Meta:
    ordering=['posted_on']    

  def __str__(self):
    return self.image_name  

  @classmethod
  def get_images_all(cls):
    '''
    function that gets all images posted
    '''    
    posts=cls.objects.order_by('-id')
    return posts

  @classmethod
  def single_image(cls,image_id):
    '''
    function gets a single image posted by id
    '''
    image_posted=cls.objects.get(id=image_id)
    return image_posted

  @classmethod
  def get_image_id(cls,imageId):
    '''
    function that gets an image id    
    '''
    image_id=cls.objects.filter(id=imageId)
    return image_id

  @classmethod
  def get_user_posts(cls,user_id):
    '''
    function that gets user's posts
    '''
    posts=cls.objects.filter(posted_by__id__contains=user_id).order_by('-id')
    return posts
  @classmethod
  def get_posts_by_name(cls, search_term):
    '''
    function tha searches for posts with a similar name
    '''
    posts=cls.objects.filter(image_name__icontains=search_term)
    return posts

class Comments(models.Model):
  '''
  class that defines how comments for a post are to be stored
  '''
  body=models.CharField(max_length=1000)
  image_id=models.ForeignKey(ImagePost, on_delete=models.CASCADE)
  posted_by=models.ForeignKey(User, on_delete=models.CASCADE)
  posted_on=models.DateField(auto_now_add=True)

  def __str__(self):
    return self.posted_by

  @classmethod
  def get_user_comments(cls, id):
    '''
    function that gets all comments
    '''
    comments=cls.objects.filter(image_id__in=id)
    return comments




