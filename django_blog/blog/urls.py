from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),  
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='edit_comment'),  
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),  
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
]
