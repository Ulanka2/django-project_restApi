from django.urls import path
from tasks.views import NewsListView, NewsDetailGenericView

urlpatterns = [
    path('', NewsListView.as_view()),
    path('<int:id>/detail/', NewsDetailGenericView.as_view()),


]