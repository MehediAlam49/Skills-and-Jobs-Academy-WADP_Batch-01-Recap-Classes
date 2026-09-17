from django.urls import path
from Recipe.views import *

urlpatterns = [
    path('', Registration_page, name='Registration_page'),
    path('Login_page/', Login_page, name='Login_page'),
    path('logout_page/', logout_page, name='logout_page'),

    path('home/', home, name='home'),
]
