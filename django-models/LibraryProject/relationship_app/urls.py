from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from . import views
from .views import register
from django .contrib.auth.views import LoginView
from django .contrib.auth.views import LogoutView

urlpatterns = [
    # URL pattern for the function-based view to list all books
    path('list_books/', list_books , name='list_books'),

    # URL pattern for the class-based view to display books in a specific library
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register.as_view(),name="register"),
    path('login/',LoginView.as_view(template_name='relationship_app/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='relationship_app/logout.html'),name='logout'),
    path('admin/',views.admin_view,name='admin_view/'),
    path('librarian/',views.librarian_view,name='librarian_view/'),
    path('member/',views.member_view,name='member_view/'),
    path('add/',views.add_book,name='add_book/'),
    path('edit/int:pk/',views.edit_book,name='edit_book/'),
    path('delete/int:pk/',views.delete_book,name='delete_book/'),

]