from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, views
from rest_framework import generics, permissions, pagination
from django.db import transaction

from users.serializers import StayWiseUserSerializer, LoginSerializer, UpdatePasswordSerializer, RegisterSerializer, LogoutSerializer
from  users.models import StayWiseUser

class StayWiseUserRegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        with transaction.atomic():
            user = request.data
            if "email" not in request.data:
                return Response({"error": "email is required"}, status=status.HTTP_400_BAD_REQUEST)
            if "password" not in request.data:
                return Response({"error": "password is required"}, status=status.HTTP_400_BAD_REQUEST)
            if "firstName" not in request.data:
                return Response({"error": "firstName is required"}, status=status.HTTP_400_BAD_REQUEST)
            if "lastName" not in request.data:
                return Response({"error": "lastName is required"}, status=status.HTTP_400_BAD_REQUEST)
            email = request.data['email']
            if StayWiseUser.objects.filter(email=email).exists():
                return Response({"error": "Email address already exists."}, status=status.HTTP_400_BAD_REQUEST)
            serializer = self.serializer_class(data=user)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StayWiseUserLoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StayWiseUserLogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StayWiseUserView(ModelViewSet):
    queryset = StayWiseUser.objects.all()
    serializer_class = StayWiseUserSerializer
    pagination_class = pagination.PageNumberPagination
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        current_user = request.user
        if not current_user.is_active:
            return Response({"error": "user is not active"}, status=status.HTTP_400_BAD_REQUEST)
        if not current_user.isVerified:
            return Response({"error": "user is not verified"}, status=status.HTTP_400_BAD_REQUEST)
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        current_user = request.user
        if not current_user.is_active:
            return Response({"error": "user is not active"}, status=status.HTTP_400_BAD_REQUEST)
        if not current_user.isVerified:
            return Response({"error": "user is not verified"}, status=status.HTTP_400_BAD_REQUEST)
        user = StayWiseUser.objects.get(id=kwargs['pk'])
        serializer = StayWiseUserSerializer(
            user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        current_user = request.user
        if not current_user.is_active:
            return Response({"error": "user is not active"}, status=status.HTTP_400_BAD_REQUEST)
        if not current_user.isVerified:
            return Response({"error": "user is not verified"}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        current_user = request.user
        if not current_user.is_active:
            return Response({"error": "user is not active"}, status=status.HTTP_400_BAD_REQUEST)
        if not current_user.isVerified:
            return Response({"error": "user is not verified"}, status=status.HTTP_400_BAD_REQUEST)
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        current_user = request.user
        if not current_user.is_active:
            return Response({"error": "user is not active"}, status=status.HTTP_400_BAD_REQUEST)
        if not current_user.isVerified:
            return Response({"error": "user is not verified"}, status=status.HTTP_400_BAD_REQUEST)
        userId = kwargs['pk']
        user = StayWiseUser.objects.filter(id=userId)
        if user.exists():
            user = user.first()
            user.is_active = False
            user.save()
            return Response({
                "message": "user deleted successfully"
            }, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({
                "error": "user not found"
            }, status=status.HTTP_400_BAD_REQUEST)