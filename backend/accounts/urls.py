from django.urls import path, include
from rest_framework import routers
from knox import views as knox_views

from .api import RegisterAPI, LoginAPI, UserAPI, PermissionViewSet, PermissionGroupViewSet

# router
router = routers.DefaultRouter()
router.register('api/v2.0/auth/permissions', PermissionViewSet, 'Permissions')
router.register('api/v2.0/auth/permissiongroups', PermissionGroupViewSet, 'Permission Groups')

urlpatterns = [
    path('api/v2.0/auth/user', UserAPI.as_view()),
    path('api/v2.0/auth/login', LoginAPI.as_view()),
    path('api/v2.0/auth/register', RegisterAPI.as_view()),
    path('api/v2.0/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/v2.0/auth/logoutall', knox_views.LogoutAllView.as_view(), name='knox_logout'),
    path('', include(router.urls)),
    path('api/v2.0/auth', include('knox.urls')),
]
