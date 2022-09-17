"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
    path('api/school/<int:id>/',
    core_views.SchoolAPIView.as_view(),name = "school"
    ),
    path('api/delete-school/<int:id>/',
    core_views.SchoolDeleteAPIView.as_view(),name = "delete-school"
    ),
    path('api/update-school/<int:id>/',
    core_views.SchoolUpdateAPIView.as_view(),name = "update-school"
    ),
    path('api/collage/',
    core_views.CollageAPIView.as_view(),name = "collage"
    ),
    path('api/delete-collage/<int:id>/',
    core_views.CollageDeleteAPIView.as_view(),name = "delete-collage"
    ),
    path('api/update-collage/<int:id>/',
    core_views.UpdateCollageAPIView.as_view(),name = "update-collage"
    ),
    path('api/student/',
    core_views.StudentAPIView.as_view(),name = "student"
    ),
    path('api/subject/',
    core_views.SubjectAPIView.as_view(),name = "subject"
    ),
    path('api/subject-delete/<int:id>/',
    core_views.SubjectDeleteAPIView.as_view(),name = "subject-delete"
    ),
    path('api/subject-update/<int:id>/',
    core_views.SubjectUpdateAPIView.as_view(),name = "subject-update"
    ),
    path('api/standard/',
    core_views.StandardAPIView.as_view(),name = "standard"
    ),
    path('api/course/',
    core_views.CourseAPIView.as_view(),name = "course"
    ),
    path('api/indexview/',
    core_views.IndexAPIView.as_view(),name = "index-view"
    ),
    
    
]

