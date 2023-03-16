from django.urls import path
from . import views

urlpatterns = [
    path("test/", views.welcome),
    path("r/", views.get_request),
    path("ps", views.validate_data)
]
