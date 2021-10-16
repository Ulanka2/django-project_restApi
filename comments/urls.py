# from django.urls import path
# from comments.views import  CommentsListView, CommetsDetailGenericView

# urlpatterns = [
#     path('', CommentsListView.as_view()),
#     path('<int:id>/detail/', CommetsDetailGenericView.as_view()),
# ]

from rest_framework.routers import SimpleRouter
from comments.views import  CommentsListViewSet

router = SimpleRouter()

router.register('comments', CommentsListViewSet)

urlpatterns = []

urlpatterns += router.urls