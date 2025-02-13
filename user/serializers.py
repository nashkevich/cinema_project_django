from django.contrib.auth.models import User
from rest_framework import serializers
from .models import LikedMoviesUser

class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    password_confirm = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords must match!")
        
        data.pop('password_confirm')
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username']

class BasketSerializer(serializers.ModelSerializer):
    # basket = serializers.JSONField()
    class Meta:
        model = LikedMoviesUser
        fields = ['id','basket','user_id']