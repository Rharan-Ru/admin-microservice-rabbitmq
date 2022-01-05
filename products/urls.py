from django.urls import path
from .views import ProductViewSet, UserView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
urlpatterns = [
    path('users', UserView.as_view(), name='users-view')
] + router.urls

# urlpatterns = [
#     path('products', ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
#     path('products/<str:pk>', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
#     path('users', UserView.as_view(), name='users-view')
# ]
