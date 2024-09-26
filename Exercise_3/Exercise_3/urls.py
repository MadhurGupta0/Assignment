from django.contrib import admin
from django.urls import path
from.views import index, home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('base/', index, name="base"),

]
