from  list import views
from django.urls import path
urlpatterns = [
    path("create/", views.UrlShortCreateView.as_view()),
    path("redirect/<str:short_url>/",views.UrlRedirectView.as_view())
]
