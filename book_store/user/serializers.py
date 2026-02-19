from .models import User
from rest_framework import serializers

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =["username","password","phone_number"]
        extra_kwargs = {"password":{"write_only":True}}

    def create(self, validated_data):
        user = User(
            phone_number=validated_data['phone_number'],
            username=validated_data['username']
        )

        return user
