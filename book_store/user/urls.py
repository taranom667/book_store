from .views import *
from django.urls import path

urlpatterns = [
    path('signup', RegisterUserApi.as_view()),
    path('all_uesrs', UsersApi.as_view()),
    path('CreateAuthor',CreateAuthorApi.as_view()),

]
