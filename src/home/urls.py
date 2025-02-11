from django.contrib import admin
from django.urls import path

from .views import home_view, about_page
from auth import views as auth_views

urlpatterns = [
    path("", home_view),
    path("login/", auth_views.login_view),
    path("register/", auth_views.register_view),
    path('admin/', admin.site.urls),
    path("about/", about_page),

]
