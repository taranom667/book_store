from django.shortcuts import render, redirect
import json
from django.http import HttpResponse, JsonResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny


def current_datetime(request):
    print('request method is', request.method)
    now = datetime.datetime.now()
    html = 'this is MFT'
    return HttpResponse(html)


def current_datetime2(request):
    print('request method is', request.method)
    now = datetime.datetime.now()
    html = 'this is MFT sec'
    return HttpResponse(html)


def get_all_books(request):
    books = list(Book.objects.values_list())
    return JsonResponse(books, safe=False)


def index(request):
    return render(request, 'base.html')


@csrf_exempt
def create_book(request):
    if request.method == "POST":
        body = json.loads(request.body.decode("utf-8"))
        body["published_date"] = "2026-01-02"
        book = Book.objects.create(**body)
        try:
            return JsonResponse({"book_id": book.id})
        except:
            pass
        return JsonResponse({"error": "Data format is not correct"})

    elif request.method == "GET":
        books = list(Book.objects.values_list())
        return JsonResponse(books, safe=False)
    elif request.method == "DELETE":
        pass
    elif request.method == "PUT":
        pass


class BookAPI(APIView):

    def post(self, request):
        body = json.loads(request.body.decode("utf-8"))
        body['published_date'] = datetime.datetime.now().date()
        serializer = BookSerializer(data=body)
        if serializer.is_valid():
            book = serializer.save()
            return JsonResponse({"book_id": book.id})
        return JsonResponse({"error": "Data format is not correct"})

    def get(self, request):
        books = list(Book.objects.values_list())
        return JsonResponse(books, safe=False)


class BookAPIList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class PublishedBookAPIList(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.filter(is_published=True)

class BOOKGenericsAPICreate(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BookSerializer


    # queryset = Book.objects.annotate(total_images=Count('image_query'))


class CreateImageeBookAPI(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    permission_classes = (AllowAny,)
    serializer_class = ImageSerializer
    queryset = Book.objects.filter()
    def add_image(self, request, book_id):
        serializer_class = ImageSerializer(data=request.data)
        book = Book.objects.get(id=book_id)
        if serializer_class.is_valid():
                image1=ImageBook.objects.create(
                book=book,
                image=request.FILES['image'],
                name = request['name'],
                description = request['description'])
                image1.save()
                book.image_book.add(image1)
                return JsonResponse({"image_id": image1.id , "book_id": book_id})
        else:
                serializer_class = ImageSerializer()
                return render(request, 'book_image.html', {'form': serializer_class})


class BookGenericsAPIUpdate(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    permission_classes = (AllowAny,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class GetOneBookAPI(generics.RetrieveAPIView):
    lookup_field = 'id'
    permission_classes = (AllowAny,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class DeleteBookAPI(generics.RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)
    queryset = Book.objects.all()
