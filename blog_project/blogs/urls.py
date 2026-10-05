from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.UpdateProfile_view, name='update_profile'),
    path('user-list/', views.user_list_view, name='user_list'),

    path('home/', views.home_view, name='home'),
    path('blogs/', views.blog_list_view, name='blog_list'),
    path('blog-create/', views.blog_create_view, name='blog_create'),
    path('blog-detail/<int:blog_id>/', views.blog_detail_view, name='blog_detail'),
    path('update-blog/<int:blog_id>/', views.blog_update_view, name='blog_update'),
    path('delete-blog/<int:blog_id>/', views.blog_delete_view, name='blog_delete'),
]