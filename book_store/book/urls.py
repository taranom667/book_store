from django.urls import path
from .views import *

urlpatterns = [
    path('creatbook', create_book),
    path('c', BookAPI.as_view()),
    path('date', current_datetime),
    path('book_generic', BOOKGenericsAPIGet.as_view()),
    path('book_generic_delete/<int:id>', BOOKGenericsAPIDelete.as_view()),
    path('book_generic_update/<int:id>',BOOKGenericsAPIPut.as_view()),
    path('book_generic_post/',BOOKGenericsAPIPost.as_view()),










]