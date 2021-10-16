from rest_framework import serializers

from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField(source='author.username')
    books_name = serializers.ReadOnlyField(source='books.title')

    class Meta:
        model = Comment
        fields = ['id', 'name', 'books_name', 'content', 'creation_date', ]
        read_only_fields = ['creation_date', ]

