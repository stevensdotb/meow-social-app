from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from .models import Post
from .forms import PostForm


def user_profile(request, username):

    user_lookup = User.objects.filter(username=username).first()
    if not user_lookup:
        return redirect("not_found_404")

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = Post(**form.cleaned_data, user=request.user)
            new_post.save()
            return redirect("user_profile", username=username)

    form = PostForm()
    posts = Post.objects.filter(user__username=username).all().order_by("-created_at")

    context = {
        "username": username,
        "posts": posts,
        "form": form
    }
    return render(request, "profile.html", context)
