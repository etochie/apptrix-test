from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from apps.core.models import Contacts


class UserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(
        max_length=255, read_only=True, source='auth_token.key'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'token']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Создание пользователя с токеном и отправка активации по почте"""
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=make_password(validated_data['password']),
            is_active=False
        )
        data = self.get_initial()
        data['token'] = Token.objects.create(user=user)
        user.refresh_from_db()

        # активация по почте
        from_email = Contacts.objects.last().email
        token = Token.objects.get(user=user)
        send_mail(
            'Активируйте аккаунт',
            'http://localhost/activate/{0}/{1}'.format(user.pk, token),
            from_email=from_email,
            recipient_list=(user.email,),
            fail_silently=False,
        )
        return user
