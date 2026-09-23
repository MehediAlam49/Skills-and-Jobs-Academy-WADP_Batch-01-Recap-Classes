from django.urls import path
from jobPortal.views import *

urlpatterns = [
    path('', register_view, name='register_view'),
    path('login_view/', login_view, name='login_view'),
    path('logout_view/', logout_view, name='logout_view'),
    path('dashboard_view/', dashboard_view, name='dashboard_view'),
    path('profile_view/', profile_view, name='profile_view'),
    path('update_profile_view/', update_profile_view, name='update_profile_view'),
]
