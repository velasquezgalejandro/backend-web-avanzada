from rest_framework import viewsets
from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
