from .models import User
from rest_framework import serializers

class RegisterUserSerializer(serializers.ModelSerializer):
    shamsi_birth_day = serializers.SerializerMethodField(read_only=True)
    def get_shamsi_birth_day(self, obj):
        return "1404-11-23"


    class Meta:
        model = User
        fields =["username","password","phone_number","national_code","shamsi_birth_day"]
        extra_kwargs = {"password":{"write_only":True}}

    def create(self, validated_data):
        user = User(
            phone_number=validated_data['phone_number'],
            username=validated_data['username'],
            national_code=validated_data['national_code']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_national_code(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("National code must be at least 11 digits")
        else:
            return value