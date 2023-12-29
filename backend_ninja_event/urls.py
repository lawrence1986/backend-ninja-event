"""
URL configuration for backend_ninja_event project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.http import  JsonResponse
from django.views import View

class About(View):
    def get(self, request, *args, **kwargs):
        data = {"gender":"Male", "github_url":"github.com/lawrence1986", "name":"Lawrence Maduabuchi"}
        return JsonResponse(data)

urlpatterns = [
    path('about/', About.as_view(), name="about")
]