"""
URL configuration for cinema_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework import routers
from movies import movie_views
from user import user_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
router = routers.DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("movie",movie_views.MovieApiView.as_view()),
    path("movie/<str:id>",movie_views.MovieApiView.as_view()),
    path("register",user_views.UserRegistrationViews.as_view()),
    path("user_info",user_views.GetUserView.as_view()),
    path("user/basket",user_views.BasketUserView.as_view()),
    path("api/token",TokenObtainPairView.as_view()),
    path("api/token/refresh",TokenRefreshView.as_view())
]
urlpatterns += router.urls