from django.urls import path, include

from . import views

urlpatterns = [
    path("<str:username>/", views.profile_view),
]
