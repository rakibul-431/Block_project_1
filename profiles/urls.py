from django.urls import path
from profiles import views
urlpatterns = [
    path('add_profile/',views.profile_add,name='add_profile')
]
