from django.urls import path
from blog.views import ArticleView, CommentView, ArticleListView, ArticleDetailView

urlpatterns = [
    path('articles/', ArticleView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleView.as_view(), name='article-detail'),
    path('articles/<int:article_id>/comments/', CommentView.as_view(), name='comment-list'),
    path('articles/<int:article_id>/comments/<int:pk>/', CommentView.as_view(), name='comment-detail'),
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]
