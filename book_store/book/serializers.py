from http.client import responses

from rest_framework import serializers
from book.models import Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        data['published_date'] = datetime.datetime.now().date()
        print('data',data)
        data=super().to_internal_value(data=data)
        print(data)
        return data
    def validate(self, data):
        if True:
            res=super().validate(attrs=data)
            return res

    def to_representation(self, instance):
        respond=super().to_representation(instance=instance)
        #print(type(respond['published_date']))
        #respond['published_date'] = '1404-09-09'
        return respond

    class Meta:
        model = Book
        fields ="__all__"