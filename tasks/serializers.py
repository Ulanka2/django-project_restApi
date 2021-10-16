from tasks.models import Books
from rest_framework import serializers
from django.contrib.auth import get_user_model
from comments.serializers import CommentSerializer


class BooksSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Books
        fields = ['id', 'author', 'title', 'description', 'amount_of_upvotes', 'creation_date', 
                  'comments', ]
        read_only_fields = ['amount_of_upvotes', 'creation_date', ]