from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("cr/", include("crud.urls")),
    path("", include("project.urls")),
    path('admin/', admin.site.urls),
    path("practice/", include("practice.urls"))
]
