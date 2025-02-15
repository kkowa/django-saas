from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth import get_user_model

User = get_user_model()


@login_required
def profile_view(request, username=None, *args, **kwargs):
    user = request.user
    # profie_user_object = User.objects.get(username=username)
    profie_user_object = get_object_or_404(User, username=username)
    is_me = profie_user_object == user
    return HttpResponse(f"Hello there {username} - {profie_user_object.id} - {user.id} - {is_me}")
