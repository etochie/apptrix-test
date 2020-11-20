from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework import mixins
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from apps.users.serializers import UserSerializer


class UserView(
    mixins.CreateModelMixin,
    GenericViewSet
):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserActivate(APIView):
    def get(self, request, pk, token):
        try:
            user = User.objects.get(pk=pk)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user == Token.objects.get(key=token).user:
            user.is_active = True
            user.save()
        return redirect('landing_url')
