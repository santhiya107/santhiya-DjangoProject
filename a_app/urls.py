
from . import views

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('profile',views.profile,name="profile"),
    path('update_profile',views.update_profile,name="update_profile"),
    path('view_profile',views.view_profile,name="view_profile"),
    path('logged',views.logged,name="logged"),
    path('delete_user',views.delete_user,name="delete_user"),
   
    
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
