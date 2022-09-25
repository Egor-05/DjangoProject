from django.urls import path
from django.contrib import admin
from .views import MainPage

urlpatterns = [
    path("admin", admin.site.urls),
    path("home", MainPage.as_view())
]