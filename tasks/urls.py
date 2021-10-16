from rest_framework.routers import SimpleRouter

from tasks.views import BooksViewSet


router = SimpleRouter()

router.register('books', BooksViewSet )

urlpatterns = []

urlpatterns += router.urls