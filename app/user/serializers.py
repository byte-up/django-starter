from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.conf import settings
from django.contrib.sites.models import Site
from dj_rest_auth.models import TokenModel

from .models import *
from utils.drf_errors.mixins import FriendlyErrorMessagesMixin


class UserSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'last_login', 'first_name', 'last_name', 'email', 'date_joined')
        model = User


class UserRegistrationSerializer(FriendlyErrorMessagesMixin, RegisterSerializer):
    first_name = serializers.CharField(max_length=255, required=True)
    last_name = serializers.CharField(max_length=255, required=True)

    def custom_signup(self, request, user):
        if self.validated_data.get('first_name', None):
            user.first_name = self.validated_data.get('first_name', '')
        if self.validated_data.get('last_name', None):
            user.last_name = self.validated_data.get('last_name', '')
        user.save(update_fields=['first_name', 'last_name'])


class UserDetailsSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    key = serializers.SerializerMethodField('is_key', read_only=True)
    user = serializers.SerializerMethodField('is_user', read_only=True)

    def is_key(self, obj):
        token = TokenModel.objects.filter(user=obj).first()
        if not token:
            token = TokenModel.objects.create(user=obj)
        return str(token)

    def is_user(self, obj):
        serializers = UserSerializer(obj)
        return serializers.data

    class Meta:
        fields = ('user', 'key')
        model = User


class TokenSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TokenModel
        fields = '__all__'

class NotificationSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Notification
