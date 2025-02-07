from django.contrib.auth.models import User
from rest_framework import serializers

class UserRegistrationSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True,required=True)
    password_confirm = serializers.CharField(write_only=True,required=True)

    class Meta:
        model = User
        fields = ['username','email','password']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Password must match!")
        return data
    
    def create(self,validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user