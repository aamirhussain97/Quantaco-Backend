from django.urls import path
from .views import user_login, user_logout, save_user, is_logged_in

urlpatterns = [
    path('api/login/', user_login, name='user_login'),
    path('api/logout/', user_logout, name='user_logout'),
    path('api/save_user/', save_user, name='save_user'),
    path('api/isloggedin/', is_logged_in, name='is_logged_in'),
]
