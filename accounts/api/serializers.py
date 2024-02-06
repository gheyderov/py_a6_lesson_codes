from typing import Any, Dict
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name'
        )


class UserPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)
        user_serializer = UserProfileSerializer(self.user)
        data.update(user_serializer.data)
        return data