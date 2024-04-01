from django.urls import path
from blog.views import PostCreateView,PostListView,PostDetailsView,PostUpdateView,PostDeleteView,CategoryCreateView,CommentsView
urlpatterns = [
    path('post-list/', PostListView, name="PostListView"),
    path('create-post/', PostCreateView, name="PostCreateView"),
    path('details-post/<int:id>/', PostDetailsView, name="PostDetailsView"),
    path('update-post/<int:id>/', PostUpdateView, name="PostUpdateView"),
    path('delete-post/<int:id>/', PostDeleteView, name="PostDeleteView"),
    path('create-category/', CategoryCreateView, name="CategoryCreateView"),
    path('comment/', CommentsView, name="CommentsView"),
    
]
