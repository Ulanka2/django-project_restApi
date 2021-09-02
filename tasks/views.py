from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from tasks.models import News
from tasks.serializers import NewsSerializer
from rest_framework import views, generics


class NewsListView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        """Фунция для сохранение нынешным user sozdanym zadachi"""
        return serializer.save(owner=self.request.user)

    def get(self, request):
        news = News.objects.all()
        serializers = NewsSerializer(news, many=True)
        return Response(serializers.data)



class NewsDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'id'




# class NewsAPIView(APIView):
#     permission_classes = [IsAuthenticated,]

#     def get(self, request):
#         news = News.objects.all()
#         serializers = NewsSerializer(news, many=True)
#         return Response(serializers.data)


#     def post(self, request):
#         serializer = NewsSerializer(data=request.data )
#         if serializer.is_valid():
#             owner = request.user
#             news = News.objects.create(
#             owner=owner,
#             title=serializer.validated_data.get('title'),
#             body=serializer.validated_data.get('body'),
#             img=serializer.validated_data.get('img'),
#             )
#             serializer = NewsSerializer(instance=news)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
