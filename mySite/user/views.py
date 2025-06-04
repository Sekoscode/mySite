from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

# yourapp/views.py
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

class CustomLogoutView(LogoutView):
    """
    Custom logout view that renders a template on logout
    and redirects the user to the home page afterward.

    Attributes:
        template_name (str): Template to render on logout.
        next_page (str): URL to redirect to after logout.
    """
    template_name = 'logout.html'
    next_page = reverse_lazy('home')  # Redirect after logout


def home(request):
    """
    Renders the homepage for the users app.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered 'users/home.html' template.
    """
    return render(request, 'users/home.html')


def register(request):
    """
    Handles user registration.

    If the request method is POST, it processes the submitted form,
    validates it, saves the new user, and shows a success message.
    Redirects the user to the login page on successful registration.
    If the request method is GET, displays a blank registration form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered registration form template with context.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)
