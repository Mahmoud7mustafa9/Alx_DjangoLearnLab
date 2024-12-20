# notifications/urls.py
from django.urls import path
from .views import NotificationListView, MarkNotificationAsReadView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications_list'),
    path('<int:pk>/read/', MarkNotificationAsReadView.as_view(), name='mark_notification_read'),
]
