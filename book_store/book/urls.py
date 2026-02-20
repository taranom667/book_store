from django.urls import path
from .views import *

urlpatterns = [
    path('creatbook', create_book),
    path('c', BookAPI.as_view()),
    path('date', current_datetime),
    path('book_generic', BOOKGenericsAPIGet.as_view()),
    path('CreateBook',BOOKGenericsAPIGet.as_view()),
    #path('CreateImageBook',)
    #path('ShowPublishedBook',)
    #path('book',)










]