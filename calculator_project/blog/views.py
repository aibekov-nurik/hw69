from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, render
from blog.models import Article, Comment
from .serializers.article_serializers import ArticleSerializer
from .serializers.comment_serializers import CommentSerializer


class ArticleView(APIView):

    def get(self, request, pk=None):
        if pk:
            article = get_object_or_404(Article, pk=pk)
            serializer = ArticleSerializer(article)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response({'id': pk}, status=status.HTTP_204_NO_CONTENT)


class CommentView(APIView):

    def get(self, request, article_id, pk=None):
        if pk:
            comment = get_object_or_404(Comment, pk=pk, article_id=article_id)
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            comments = Comment.objects.filter(article_id=article_id)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, article_id):
        data = request.data.copy()
        data['article'] = article_id
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, article_id, pk):
        comment = get_object_or_404(Comment, pk=pk, article_id=article_id)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, pk):
        comment = get_object_or_404(Comment, pk=pk, article_id=article_id)
        comment.delete()
        return Response({'id': pk}, status=status.HTTP_204_NO_CONTENT)


class ArticleListView(View):
    def get(self, request):
        articles = Article.objects.all()
        return render(request, 'articles_list.html', {'articles': articles})

class ArticleDetailView(View):
    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        comments = Comment.objects.filter(article=article)
        return render(request, 'article_detail.html', {'article': article, 'comments': comments})