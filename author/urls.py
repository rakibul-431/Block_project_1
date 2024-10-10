from django.urls import path
from author import views
urlpatterns = [
    path('SignUp_page/',views.Rejistration,name="SignUp_page"),
    path('login_page',views.user_login,name="login_page"),
    path('logout/',views.user_logout,name='logout_page'),
    path('profile_page',views.profiel,name='profile_page'),
    path('profileUpdata',views.updateprofile,name='profileUpdata'),
    path('password_change',views.UserpasswordChange,name='passwordChange')
]
