from django.shortcuts import render
from rest_framework.response import Response
from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import  generics
from rest_framework.viewsets import ModelViewSet


# class CommentsListView(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated,]
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


#     def get(self, request):
#         comment = Comment.objects.all()
#         serializers = CommentSerializer(comment, many=True)
#         return Response(serializers.data)


# class CommetsDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated,]
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     lookup_field = 'id'

class CommentsListViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,]