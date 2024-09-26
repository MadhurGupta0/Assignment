
from django.contrib import admin
from django.urls import path
from.views import index, dynamic_content

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('home/', dynamic_content),
]
