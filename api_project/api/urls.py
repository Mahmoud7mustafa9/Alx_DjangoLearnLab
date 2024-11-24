from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]


# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router instance
router = DefaultRouter()
# Register the BookViewSet with the router
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Include the router URLs for the BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]

# api/urls.py
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # Import DRF's built-in view

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token retrieval endpoint
    path('', include(router.urls)),  # Include the rest of your API's URLs
]
