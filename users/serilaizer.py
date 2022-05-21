from asyncore import write
from dataclasses import field
import email
from .models import CustomUser
from rest_framework import serializers
from rest_framework.response import Response
from phonenumber_field.serializerfields import PhoneNumberField
from random import randint


class UserModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=80)
    phone_number = PhoneNumberField(allow_null=False, allow_blank= False)
    password = serializers.CharField(min_length=8, write_only=True)
    tradeID = serializers.CharField(max_length=100,read_only=True)
    

    class Meta:
        model = CustomUser
        fields = ['id','username', 'email', 'phone_number', 'tradeID', 'password']
        extra_kwargs = {
            'password': {'write_only':True},
            # 'tradeID': {'read_only': True}
        }
    def validate(self,to_validate):
        username = CustomUser.objects.filter(username= to_validate['username'])
        email = CustomUser.objects.filter(email=to_validate['email'])
        phone = CustomUser.objects.filter(phone_number=to_validate['phone_number'])

        if username:
            raise serializers.ValidationError(detail="Please Username already exist")
        elif email:
            raise serializers.ValidationError(detail="Please Email already exist")
        elif phone:
            raise serializers.ValidationError(detail="Please Phone number already exist")
        return super().validate(to_validate)
            
   
        

    def create(self, users_data):
        trade_id = randint(1234567,7654321)
        password = users_data.pop('password', None)
        users_instance = self.Meta.model(**users_data)
        if password is not None:
            users_instance.tradeID = f"TV{trade_id}"
            users_instance.set_password(password)
        users_instance.save()
        return users_instance
       


class VerifyOtpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    otp = serializers.CharField()
    class Meta:
        model = CustomUser
        field = ['email', 'otp']



class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser
    email = serializers.EmailField()
    new_password = serializers.CharField(write_only=True)
   
