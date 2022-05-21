import email
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from users.email_verification import send_otp_to_email

from users.models import CustomUser
from users.serilaizer import ChangePasswordSerializer, UserModelSerializer, VerifyOtpSerializer
# Create your views here.


class UserSignUP(generics.GenericAPIView):
    serializer_class = UserModelSerializer

    def post(self, request):
        data = request.data
        serializer = UserModelSerializer(data=data)
        if serializer.is_valid(): 
           
            serializer.save()
            otp_email = serializer.validated_data['email']
            print(otp_email)
            send_otp_to_email(email_to=otp_email)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED) 


               
        return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)   

users_signUp = UserSignUP.as_view()





class VerifyEmail(generics.GenericAPIView):

    def post(self,request):
        
        data = request.data
        serializer = VerifyOtpSerializer(data=data)
       
        if serializer.is_valid():
            user_email = CustomUser.objects.filter(email=serializer.data['email']).first()
            if user_email and (serializer.data['otp']==user_email.otp):
                user_email.is_verified =True
                return Response(data={
                    "status": 200,
                    "Email status": "verified",
                    "data": serializer.data
                }, status=status.HTTP_202_ACCEPTED)
            
            else:
                return Response(data={
                    "status": 400,
                    "OTP": "Wrong",
                    "data": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data=serializer.errors)




verifyEmail = VerifyEmail.as_view()
        

class ChangePassword(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer

    def update(self, request):
        data = request.data 
        serializer = ChangePasswordSerializer(data=data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['new_password']
            user = CustomUser.objects.filter(email= email).first()
            if user:
                user.set_password(password)
                user.save()
            
                return  Response(data={"Message": "Password changed Succesfully", "data": serializer.data})
            else:
                return Response(data={"Message": "Email Does not Exist", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return  Response(data={"Message": "Password changed Not Succesfull", "data": serializer.errors})



changePassword = ChangePassword.as_view()