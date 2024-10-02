from django.urls import path
from post import views
urlpatterns = [
    path('post/',views.post,name='post'),
    path('edit_post/<int:id>',views.edit_post,name='post_edit'),
    path('delete_post/<int:id>',views.post_delete,name="post_delete"),
]
