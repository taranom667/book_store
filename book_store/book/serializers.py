from django.contrib.admin.utils import lookup_field
from rest_framework import serializers
from .models import Book, ImageBook

class BookSerializer(serializers.ModelSerializer):
    # images=BookImagesSerializer(many=True,read_only=True)
    # images = StringRelatedField(many=True, read_only=True)

    def to_internal_value(self, data):
        data = super().to_internal_value(data=data)
        return data

    def validate(self, data):
        if True:
            res = super().validate(attrs=data)
            return res

    def get(self, request):
        return Book.objects.all()

    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        book.save()
        return book

    def to_representation(self, instance):
        respond = super().to_representation(instance=instance)
        # print(type(respond['published_date']))
        # respond['published_date'] = '1404-09-09'
        return respond

    class Meta:
        model = Book
        fields =['name','published_date','price','category','is_published','author','image_book']



class  ImageSerializer(BookSerializer):
    class Meta:
        model = ImageBook
        fields = '__all__'

    def get(self, request):
            return ImageBook.objects.all()
    def create(self, validated_data):
        pass


class ShowUserBooksSerializer(BookSerializer):
     pass

