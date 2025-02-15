from django.contrib import admin
from django.urls import path, include

from .views import home_view, pw_protected_view, user_only_view, staff_only_view
from auth import views as auth_views

urlpatterns = [
    path("", home_view, name="home"),
    path("login/", auth_views.login_view),
    path("register/", auth_views.register_view),
    path('accounts/', include('allauth.urls')),
    path('protected/', pw_protected_view),
    path('protected/user-only', user_only_view),
    path('protected/staff-only', staff_only_view),
    path('profiles/', include('profiles.urls')),

    path('admin/', admin.site.urls),
]
