from django.urls import path
from .views import *
from .views_api import *

urlpatterns = [
    path('home/', api_home, name='api_home'),
    path('createnamespace/', create_namespace, name="api_createnamespace")
]