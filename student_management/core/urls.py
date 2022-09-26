"""student_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from core import views as core_views


urlpatterns = [
    path('index',core_views.IndexView.as_view(),name= 'index'),
    path('index/edit/',core_views.IndexUpdateView.as_view(),name='index-edit'),
    path('api/collage/',
    core_views.CollageAPIView.as_view(),name = "collage"
    ),
    path('api/delete-collage/<int:id>/',
    core_views.CollageDeleteAPIView.as_view(),name = "delete-collage"
    ),
    path('api/update-collage/<int:id>/',
    core_views.UpdateCollageAPIView.as_view(),name = "collage-collage"
    ),
    
 
]