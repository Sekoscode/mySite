from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def post_list_view(request):
    post_list = Post.objects.all()  # Get all books from the database
    return render(request, 'blog.html', {'list_of_posts' : post_list })


def post_detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog_detail.html', {'post': post})
