from .models import User
from rest_framework import serializers


class RegisterUserSerializer(serializers.ModelSerializer):
    '''shamsi_birth_day = serializers.SerializerMethodField(read_only=True)
    def get_shamsi_birth_day(self, obj):
        return "1404-11-23"'''

    def to_internal_value(self, data):
        data = super().to_internal_value(data=data)
        return data

    class Meta:
        model = User
        fields = ["username", "phone_number", "password", "national_code"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            national_code=validated_data['national_code'])

        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, data):
        if True:
            res = super().validate(attrs=data)
            return res

    def to_representation(self, instance):
        respond = super().to_representation(instance=instance)
        return respond

    def validate_national_code(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("National code must be at least 11 digits")
        else:
            return value

    def to_representation(self, instance):
        data = super().to
