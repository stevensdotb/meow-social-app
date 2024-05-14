from django.shortcuts import redirect, render

from .models import Post
from .forms import PostForm


def user_profile(request, username):

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
