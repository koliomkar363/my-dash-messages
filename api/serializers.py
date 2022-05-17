from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserMessage


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserMessageSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = UserMessage
        fields = ['id', 'message', 'created_at', 'updated_at', 'created_by']
