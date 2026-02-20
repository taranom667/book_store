from django.shortcuts import render
from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
from .models import Book
from rest_framework.views import APIView
from .serializers import BookSerializer
from rest_framework import generics
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated,AllowAny


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


class BOOKGenericsAPIGet(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    #queryset = Book.objects.annotate(total_images=Count('image_query'))


class BOOKGenericsAPIDelete(generics.RetrieveDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'id'


class BOOKGenericsAPIPut(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BOOKGenericsAPIPost(generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
