from rest_framework.response import Response

from .models import User, Author
from rest_framework import serializers, status


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
            password=validated_data['password'])
        return user

    def to_representation(self, instance):
        respond = super().to_representation(instance=instance)
        return respond

    def validate_national_code(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("National code must be at least 11 digits")
        else:
            return value


''' def validate(self, data):
        if True:
            res = super().validate(attrs=data)
            return res'''


class RegisterAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'username', 'is_active', 'password', 'books', ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        books = validated_data.pop('books')
        author = Author.objects.create_user(password=password, **validated_data)
        author.books.set(books)
        return author

    def to_representation(self, instance):
        respond = super().to_representation(instance=instance)
        instance.is_active = True
        return respond
