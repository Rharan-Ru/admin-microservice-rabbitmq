from django.urls import path
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
urlpatterns = router.urls
print(router.urls)