from django.urls import path
from .views import login, register, logout, information, show_info, edit_info

app_name = 'customer'
urlpatterns = [
    path('login/', login),
    path('register/', register),
    path('logout/', logout),
    path('info/', information, name='info'),
    path('show_info/', show_info, name='show_info'),
    path('edit_info/', edit_info, name='edit_info'),
]
