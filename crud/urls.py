from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

urlpatterns = [
    path("mixins/<int:pk>/update-view/", views.ProductUpdateModelMixinView.as_view()),
    path("mixins/<int:pk>/delete-mixins/", views.ProductDeleteModelMixin.as_view()),
    path("mixins/<int:pk>/get-one/", views.ProductRetrieveModelMixinView.as_view()),
    path("mixins/delete-all/", views.ProductDeleteAllModelMixinView.as_view()),
    path("mixins/create-view/", views.ProductCreateModelMixinView.as_view()),
    path("mixins/get-method/", views.ProductListModelMixinView.as_view()),
    path("<int:pk>/delete/", views.ProductDeleteView.as_view()),
    path("<int:pk>/edit/", views.ProductUpdateView.as_view()),
    path("<int:pk>/", views.RetrieveProductView.as_view()),
    path("create/", views.CreateProducView.as_view()),
    path("<int:pk>/manual-update/", views.update),
    path("func/", views.retrieve_and_create),
    path("<int:pk>/delete", views.delete),
    path("auth/", obtain_auth_token),
]
