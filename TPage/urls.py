from django.urls import path
from django.contrib import admin
from .views import MainPage

urlpatterns = [
    path("admin", admin.site.urls),
    path("mainpage", MainPage.as_view())
]