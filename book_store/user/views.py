from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny


# Create your views here.
class RegisterUserApi(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
        else:
            return Response({"result": "something went wrong"}, status=200)
        return Response({"result": {"user_id": user.id}}, status=status.HTTP_200_OK)
