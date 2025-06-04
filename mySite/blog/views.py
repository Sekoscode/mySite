from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def post_list_view(request):
    """
    View to display a list of all blog posts.

    Retrieves all Post objects from the database and renders them 
    using the 'blog.html' template. The list of posts is passed 
    to the template context as 'list_of_posts'.
    """
    post_list = Post.objects.all()
    return render(request, 'blog.html', {'list_of_posts': post_list})


def post_detail_view(request, id):
    """
    View to display the details of a single blog post.

    Retrieves a single Post object based on its ID. If the post does not exist,
    returns a 404 error. The retrieved post is rendered using the 
    'blog_detail.html' template with 'post' as context variable.
    
    Args:
        request: The HTTP request object.
        id (int): The ID of the post to retrieve.

    Returns:
        HttpResponse: Rendered detail page of the post.
    """
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog_detail.html', {'post': post})
