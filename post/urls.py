from django.urls import path
from post import views
urlpatterns = [
    path('post/',views.post,name='post'),
    # path('post/',views.AddPostCreatView.as_view(),name='post'),
    path('edit_post/<int:id>',views.edit_post,name='post_edit'),
    #path('edit_post/<int:id>',views.updatePost.as_view(),name='post_edit'),
   # path('delete_post/<int:id>',views.post_delete,name="post_delete"),
    path('delete_post/<int:id>',views.deletepost.as_view(),name="post_delete"),
    path('details_post/<int:id>',views.DetailsView.as_view(),name="post_details"),
]
