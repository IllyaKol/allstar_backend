from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instant, validated_data):
        instant.first_name = validated_data.get('first_name', instant.first_name)
        instant.last_name = validated_data.get('last_name', instant.last_name)
        if 'password' in validated_data:
            instant.set_password(validated_data['password'])

        instant.save()
        return instant
