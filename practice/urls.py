from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.urls import path
from practice import views_rest

urlpatterns = format_suffix_patterns(
    [
        path("<int:pk>/snippets/", views_rest.FetchDataView.as_view()),
        path("render/", views_rest.snippet_list)
    ]
)
