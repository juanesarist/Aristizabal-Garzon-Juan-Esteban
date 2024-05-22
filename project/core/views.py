from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView
from .forms import CustomAuthentificationForm
# Create your views here.

def home(request):
    return render(request, "core/index.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthentificationForm
    template_name = "core/login.html"