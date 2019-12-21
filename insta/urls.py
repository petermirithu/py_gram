from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.home,name="Home"),
    url(r'^logout/$',views.logout_request,name="logout"),
    url(r'accounts/profile/$',views.profile,name="profile"),
    url(r'^update_profile/$',views.update_profile,name="updateProfile"),    
]
