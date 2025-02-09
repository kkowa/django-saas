from django.contrib import admin
from django.urls import path

from .views import home_view, about_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", home_view),
    path("about/", about_page),
]
