from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
from django.contrib.auth.views import LoginView
from .forms import CustomAuthentificationForm, CustomUserCreationForm
# Create your views here.

def home(request):
    return render(request, "core/index.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthentificationForm
    template_name = "core/login.html"

def signup(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "core/index.html", {"mensaje": "Usuario creado"})
    else:
        form = CustomUserCreationForm()
    return render(request, "core/signup.html", {"form": form})
