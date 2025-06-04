from django.shortcuts import render
from django.shortcuts import render


# Create your views here.
def index(request):
    """
    View for rendering the homepage or main entry point of the site.

    Renders the 'online_shop.html' template. This might serve as a default landing page.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: Rendered 'online_shop.html' page.
    """
    return render(request, "online_shop.html")


def online_shop(request):
    """
    View to render the online shop page.

    Renders the 'online_shop.html' template, possibly listing products or services.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: Rendered 'online_shop.html' page.
    """
    return render(request, "online_shop.html")


def vision_board(request):
    """
    View to render the vision board page.

    Renders the 'vision_board.html' template, which may contain user goals or inspirational content.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: Rendered 'vision_board.html' page.
    """
    return render(request, "vision_board.html")
