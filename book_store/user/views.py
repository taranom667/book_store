from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny
from .models import User
from django.db.models import Count


# Create your views here.
class RegisterUserApi(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
        else:
            return Response({"result": "something went wrong"}, status=404)
        return Response({"result": {"user_id": user.id}}, status=status.HTTP_200_OK)


'''       
       
class RegisterUserApi(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()'''


class Users(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()
