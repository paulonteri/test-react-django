from django.contrib.auth.models import Permission, Group
from knox.models import AuthToken
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response

from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, PermissionSerializer, \
    PermissionGroupSerializer


# Register API
class RegisterAPI(generics.GenericAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # send back any errors
        serializer.is_valid(raise_exception=True)
        # used to save the user
        user = serializer.save()
        # send response(RF) back
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            # create and send back token
            "token": AuthToken.objects.create(user)[1]
        })


# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # send back any errors
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        # send response(RF) back
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            # create and send back token
            "token": AuthToken.objects.create(user)[1]
        })


# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        # get user using the token in isAuthenticated
        return self.request.user


# Permissions #
# Permission API
class PermissionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()


# Permissions API
class PermissionGroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = PermissionGroupSerializer
    queryset = Group.objects.all()
