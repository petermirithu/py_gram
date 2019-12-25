from django.test import TestCase
from .models import UserProfile,ImagePost,Comments
from django.contrib.auth.models import User

class UserProfileTestCase(TestCase):
  '''
  class that tests all function in the userprofile
  '''
  def setUp(self):
    '''
    Testcase to create new user profile object for test purposes
    '''    
    self.pyra=User(username='pyra',email='pyra@yahoo.com')
    self.pyra=UserProfile(user=self.pyra,status='Feel goood',pic="pyra.png",career='Software dev')

  def test_save_profile(self):
    '''
    testcase that tests on saving a user's profile
    '''
    self.pyra.save_profile()
    users=UserProfile.objects.all()
    self.assertEquals(len(users,1))

  def tearDown(self):   
    '''
    Testcase that delete all objects after every test has run
    ''' 
    User.objects.all().delete()  
    UserProfile.all().delete()

  def test_delete_profile(self):
    '''
    test case that tests on deleting a user's profile
    '''
    self.pyra.save_profile()
    users=UserProfile.objects.all()
    self.assertTrue(len(users)==0)

  def test_search_user(self):
    '''
    test case that tests on searching for a single user
    '''
    self.pyra.save_profile()
    found=UserProfile.search_user(self.pyra.username)
    self.assertTrue(found.username=='pyra')

class ImagePostTestCase(TestCase):
  '''
  class with testcases for all function in imagepost class
  '''
  def setUp(self):
    '''
    creating new objects
    '''
    self.pyra=User(username='pyra',email='pyra@yahoo.com')
    self.pyra.save()

    self.bmw=ImagePost(image=' https://ucarecdn.com/505a47e6-769a-40d7-a4ac-b0dea6822723/',image_name="BMW series",caption='I love BMW cars',posted_by=self.pyra,posted_on='12-10-2019')

  def test_save_post(self):
    '''
    testcase that tests on saving a new post
    '''
    self.bmw.save_post()
    posts=ImagePost.objects.all()
    self.assertEquals(len(posts),1)

  def tearDown(self):   
    '''
    Testcase that delete all objects after every test has run
    '''     
    ImagePost.objects.all().delete()
    User.objects.all().delete()
        
  def test_delete_post(self):
    '''
    testcase that tests on deleting a post
    '''
    self.bmw.save_post()
    self.bmw.delete_post()
    posts=ImagePost.objects.all()
    self.assertTrue(len(posts)==0)  

  def test_update_caption(self):
    '''
    testcase that tests on updating a post's caption
    '''
    self.bmw.save_post()
    result=ImagePost.update_caption(self.bmw.id,'they are good cars')        
    self.assertTrue(result.caption,'they are good cars')

  def test_get_all_posts(self):
    '''
    testcase that tests on getting all posts
    '''
    self.bmw.save_post()
    final_res=ImagePost.get_images_all()
    self.assertEquals(len(final_res),1)

  def test_single_post(self):
    '''
    testcase that test on getting a single post
    '''
    self.bmw.save_post()
    got=ImagePost.single_image(self.bmw.id)  
    self.assertTrue(got.image_name==self.bmw.image_name)

  def test_get_image_id(self):
    '''
    testcase that tests on getting an image id
    '''
    self.bmw.save_post()
    post_id=ImagePost.get_image_id(self.bmw.id)  
    self.assertTrue(post_id.id==self.bmw.id)

  def test_get_user_posts(self):
    '''
    testcase that tests on getting a user's posts
    '''
    self.bmw.save_post()
    self.pyra.save()
    user_posts=ImagePost.get_user_posts(self.pyra.id)
    self.assertEquals(len(user_posts),1)

  def test_get_posts_by_name(self):
    '''
    testcase that tests on getting a post by name
    '''
    self.bmw.save_post()
    found=ImagePost.get_posts_by_name('BMW series')
    self.assertEquals(len(found),1)

class CommentsTestCase(TestCase):
  '''
  class that contains testcases for all function under comments class
  '''
  def setUp(self):
    '''
    creates comment object for test purposes
    '''
    self.pyra=User(username='pyra',email='pyra@yahoo.com')
    self.bmw=ImagePost(image=' https://ucarecdn.com/505a47e6-769a-40d7-a4ac-b0dea6822723/',image_name="BMW series",caption='I love BMW cars',posted_by=self.pyra,posted_on='12-10-2019')
    self.bmw.save_post()
    self.pyra.save()
    self.comment=Comments(body="I like it",image_id=self.bmw.id,posted_by=self.pyra,posted_on='09-12-2019')    

  def test_save_comment(self):
    '''
    tescase to test on saving a new comment
    '''    
    self.comment.save_comment()
    comments=Comments.objects.all()
    self.assertEquals(len(comments)==1)

  def tearDown(self):   
    '''
    Testcase that delete all objects after every test has run
    '''     
    ImagePost.objects.all().delete()
    User.objects.all().delete()
    Comment.objects.all().delete()
        
  def test_delete_comment(self):
    '''
    testcase to test on deleting a comment
    '''
    self.pyra.save()
    self.comment.save_comment()    
    self.comment.delete_comment()
    comments=Comments.objects.all()
    self.assertTrue(len(comments)==0)

  def test_get_posts_comments(self):
    '''
    testcase to test on getting comments for a specific post
    '''
    self.bmw.save_post()
    self.comment.save_comment()
    comments_found=Comments.get_post_comments(self.bmw.id)
    self.assertEquals(len(comments_found),1)

  def test_update_caption(self):
    '''
    testcase to test on updating a comment
    '''
    self.comment.save_comment()
    updated=Comments.update_caption(self.comment.id,'its legit')
    self.assertTrue(updated.body=='its legit')











