from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url('^$',views.home,name="Home"),
    url(r'^logout/$',views.logout_request,name="logout"),
    url(r'accounts/profile/$',views.profile,name="profile"),
    url(r'^update_profile/$',views.update_profile,name="updateProfile"),  
    url(r'^new_post/$',views.new_post,name="newPost"),
    path('single_post/<int:id>',views.single_post,name="singlePost"),
    url(r"^like/$",views.like_post,name="like_post"),
    url(r"^follow/$",views.follow_user,name="follow_user"),
    path('user/<username>',views.others_profile,name="otherProfile"),
]
