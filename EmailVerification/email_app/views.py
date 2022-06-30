from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from . emails import *

class RegisterView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response(
                    {   
                        'status':status.HTTP_201_CREATED,
                        'message' : 'Registration Successful, Check email',
                        'data': serializer.data, 
                    },status=status.HTTP_201_CREATED
                )
            return Response(
                {
                    'status':status.HTTP_400_BAD_REQUEST,
                    'message' : 'Registration Failed',
                    'data': serializer.errors
                }
            )
        except Exception as e:
            print(e)

class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyAccountSerializer(data=data)
            
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                
                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response(
                        {
                            'status':status.HTTP_400_BAD_REQUEST,
                            'message' : 'User does not exist',
                            'data': 'Invalid Email'
                        }
                    )
                if not user[0].otp == otp:
                    return Response(
                        {
                            'status':status.HTTP_400_BAD_REQUEST,
                            'message' : 'Invalid OTP',
                            'data': 'Invalid OTP'
                        }
                    )
                
                user = user.first()
                user.is_verified = True
                user.save()
                
                return Response(
                    {
                        'status' : status.HTTP_200_OK,
                        'message' : 'Account verified',
                        'data': {}
                    }
                )
        except Exception as e:
            print(e)        