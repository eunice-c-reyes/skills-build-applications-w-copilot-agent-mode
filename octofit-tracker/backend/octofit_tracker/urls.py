"""octofit_tracker URL Configuration

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
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from django.http import HttpResponse
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardEntryViewSet, WorkoutViewSet, api_root
import os



router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardEntryViewSet)
router.register(r'workouts', WorkoutViewSet)

urlpatterns = [
    path('', lambda request: redirect('/api/', permanent=False)),
    path('admin/', admin.site.urls),
    # API root returns available endpoints, with dynamic base URL for documentation
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
    path('-8000.app.github.dev/', lambda request: HttpResponse("GitHub Dev instance detected")),
]
