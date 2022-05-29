from rest_framework.routers import DefaultRouter
from .views import BookViewset, BookItemViewset

router = DefaultRouter()
router.register("books", BookViewset)
router.register("book_item", BookItemViewset)

urlpatterns = router.urls
