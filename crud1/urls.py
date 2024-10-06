from django.urls import path
from .views import *

urlpatterns = [
    path('home/', homepage),
    path('add_user/', add_user),
    path('delete_user/<int:user_id>/', delete_user),
    path('update_user/<int:user_id>/', update_user, name='update_user'),
]
