from http.client import responses

from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from .models import Book, ImageBook


class BookImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageBook
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    # images=BookImagesSerializer(many=True,read_only=True)
    images = StringRelatedField(many=True, read_only=True)

    def to_internal_value(self, data):
        data = super().to_internal_value(data=data)
        return data

    def validate(self, data):
        if True:
            res = super().validate(attrs=data)
            return res

    def to_representation(self, instance):
        respond = super().to_representation(instance=instance)
        # print(type(respond['published_date']))
        # respond['published_date'] = '1404-09-09'
        return respond

    class Meta:
        model = Book
        fields =['__all__']

