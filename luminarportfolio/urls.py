"""
URL configuration for luminarportfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from portfolio.views import AboutView
from portfolio.views import CoursesView
from portfolio.views import TrainersView
from portfolio.views import BranchesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("about/",AboutView.as_view()),
    path("course/",CoursesView.as_view()),
    path("trainer/",TrainersView.as_view()),
    path("branch/",BranchesView.as_view()),
]
