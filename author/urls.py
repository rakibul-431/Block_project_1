from django.urls import path
from author import views
urlpatterns = [
    path('add/',views.add_author,name="add_athor")
]
