from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('', index, name='index'),
    path('accounts/login/', login_page, name='login_page'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout')
]