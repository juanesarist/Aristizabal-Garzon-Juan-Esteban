
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "core"

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path('signup/', views.signup, name="signup"),
]

urlpatterns += staticfiles_urlpatterns()