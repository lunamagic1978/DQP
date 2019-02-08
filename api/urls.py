from django.urls import path
from .views import *
from .views_api import *

urlpatterns = [
    path('home/', api_home, name='api_home'),
    path('home/<int:namespace>/', api_homne_namespace, name="api_home_namespace"),
    path('home/<int:namespace>/<int:project>/', api_home_api, name="api_home_api"),
    path('home/<int:namespace_id>/<int:project_id>/<int:api_id>/doc', api_home_api_doc, name="api_home_api_doc"),
    path('home/<int:namespace_id>/<int:project_id>/<int:api_id>/test', api_home_api_test, name="api_home_api_test"),
    path('createnamespace/', create_namespace, name="api_createnamespace"),
    path('swagger_url/', get_swagger),
    path('openapi/', mac_openapi),
    path('gateway/', mac_gateway),
    path('create_project/', create_project),
]