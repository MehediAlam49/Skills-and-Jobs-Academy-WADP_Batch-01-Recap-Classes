from django.urls import path
from CalorieCounter.views import *

urlpatterns = [
    path('', register_page, name='register_page'),
    path('login-page/', login_page, name='login_page'),

    path('dashboard/', dashboard, name='dashboard'),
    path('logout-page/', logout_page, name='logout_page'),

    path('profile/', profile_page, name='profile_page'),
    path('update_profile/', update_profile, name='update_profile'),

    path('add-calorie/', add_calorie, name='add_calorie'),
    path('consumed-calorie/', consumed_calorie, name='consumed_calorie'),
    path('edit-calorie/<str:id>', edit_calorie, name='edit_calorie'),
    path('delete-calorie/<str:id>', delete_calorie, name='delete_calorie'),
]
