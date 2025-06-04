from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "online_shop.html",)

def online_shop(request):
    return render(request, "online_shop.html")

def vision_board(request):
    return render(request, "vision_board.html")