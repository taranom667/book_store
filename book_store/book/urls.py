from django.urls import path
from .views import *

urlpatterns = [
    #crud book
    path('DeleteBook/<int:id>',DeleteBookAPI.as_view()),
    path('CreateBook', BOOKGenericsAPICreate.as_view()),
    path('GetBook/<int:id>',GetOneBookAPI.as_view()),
    path('UpdateBook/<int:id>',BookGenericsAPIUpdate.as_view()),

    path('ShowAllBook', BookAPIList.as_view()),
    path('ShowPublishedBook', PublishedBookAPIList.as_view()),
    path('ShowUserBooks/',ShowUserBooksAPI.as_view()),
   #imagebook

    path('CreateImageBook/<int:id>',CreateImageeBookAPI.as_view()),



]
