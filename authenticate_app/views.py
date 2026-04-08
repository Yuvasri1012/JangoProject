from django.shortcuts import render
from rest_framework .views import APIView
from .serializers import *
from rest_framework_simplejwt .tokens import RefreshToken
from rest_framework.response import Response

# Create your views here.

class SignupAPI(APIView):
    def post(self,request):
        try:
            serializer = Signupserializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                refresh_token = RefreshToken.for_user(user)
                access_token = refresh_token.access_token
                return Response({
                'refresh': str(refresh_token),
                'access': str(access_token),
                'username': user.username
            })
            return Response(serializer.errors)  
        except Exception as e:
            return Response(str(e))
        