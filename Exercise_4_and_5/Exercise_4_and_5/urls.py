from django.contrib import admin
from django.urls import path
from.views import index, home,signup,lout,profile
from .form import LoginForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('base/', index, name="base"),
    path('signup/', signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm, template_name="login.html"),name="login"),
    path('logout/',lout,name="logout"),
    path('profile/',profile,name="profile"),


]
