from django.urls import path
from categories import views
urlpatterns = [
    path('category/',views.categorys,name='catagorys')
]
