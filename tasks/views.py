from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from tasks.serializers import RatingSerializer

from tasks.models import Books, Rating
from tasks.serializers import BooksSerializer
from comments.serializers import CommentSerializer


class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


    @action(methods=['post', ], serializer_class=CommentSerializer, detail=True)
    def comments(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        books = self.get_object()

        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, books=books)
            return Response(serializer.data)

    @action(methods=['post', ], detail=True)
    def upvote(self, request, *args, **kwargs):
        books = self.get_object()
        books.upvotes_amount += 1
        books.save()
        serializer = self.get_serializer_class()(instance=books)
        return Response(serializer.data)

    @action(methods=['post', ], detail=True, permission_classes=[IsAdminUser, ])
    def drop_upvotes(self, request, *args, **kwargs):
        books = self.get_object()
        books.upvotes_amount = 0
        books.save()
        serializer = self.get_serializer_class()(instance=books)
        return Response(serializer.data)


    @action(methods=['post'], detail=True, permission_classes=[IsAuthenticated, ])
    def rating(self, request, *args, **kwargs):
        books = self.get_object()
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating, created = Rating.objects.get_or_create(books=books, author=request.user,
                                              defaults={'value': serializer.validated_data['value']})
        if not created:
            rating.value = serializer.validated_data['value']
            rating.save()
        serializer = self.get_serializer(instance=books)
        return Response(serializer.data)
