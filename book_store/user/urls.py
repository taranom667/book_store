from .views import *
from django.urls import path
urlpatterns = [
    path('signup',RegisterUserApi.as_view()),
    path('all_uesrs',Users.as_view()),

]