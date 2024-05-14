

from django.shortcuts import render
from userprofile.models import Post


def home(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "templates/index.html", {"posts": posts})

def not_found_404(request):
    return render(request, 'templates/404.html')