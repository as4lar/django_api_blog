from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from .serializer import PostSerializer, CommentSerializer
from .models import Post, Comment
# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

    @action(detail=True, methods=['get'])
    def comments(self,request, pk=None):
        post=self.get_object()
        comments=post.comments.all()
        serializer=CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer