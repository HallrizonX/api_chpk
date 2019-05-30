from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile


class UserSerializers(serializers.ModelSerializer):
    """Serializer User table"""
    class Meta:
        model = User
        fields: tuple = ('username', 'email', 'is_active', 'is_superuser', 'is_staff')


class ProfileSerializers(serializers.ModelSerializer):
    """Serializer Profile table"""
    user = UserSerializers()

    class Meta:
        model = Profile
        fields: tuple = ('name', 'surname', 'last_name', 'access', 'user')


class SimpleProfileSerializers(serializers.ModelSerializer):
    """Serializer Profile table"""
    class Meta:
        model = Profile
        fields: tuple = ('name', 'surname', 'last_name', 'access')
