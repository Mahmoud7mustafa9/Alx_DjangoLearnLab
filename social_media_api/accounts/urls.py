from django.urls import path
from .views import RegisterView, ProfileView, CustomAuthToken

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]
# accounts/urls.py
from django.urls import path
from .views import FollowUserView, UnfollowUserView


