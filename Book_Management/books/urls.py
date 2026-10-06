from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('books/', home_view, name='home'),
    path('books/add/', add_book_view, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book_view, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book_view, name='delete_book'),
    path('books/<int:book_id>/', book_detail_view, name='book_detail'),
]