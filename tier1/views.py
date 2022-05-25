import email
from multiprocessing import context
from django.shortcuts import render
from rest_framework import serializers,generics,status
from tier1 import serilaizer
from rest_framework.response import Response

from tier1.serilaizer import GetAllTransactionSeriliazer, TierOneSeriealizer
# Create your views here.
from .models import TierOne
from users.models import CustomUser
from datetime import date,timedelta



class CreateTierOneTransaction(generics.CreateAPIView):
    serializer_class = TierOneSeriealizer

    def post(self, request):
        # user= request.user
        # print(user)
        serializer_class = TierOneSeriealizer
        data = request.data
        serilaizer = serializer_class(data=data, context=request) #The context passes request to the serializzer 
        if serilaizer.is_valid():
            # serilaizer.investor = user
            serilaizer.save()
            return Response(data=serilaizer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serilaizer.errors, status=status.HTTP_400_BAD_REQUEST) 
        


create_transaction_one = CreateTierOneTransaction.as_view()



class GetAllTransaction(generics.ListAPIView):
    serializer_class = GetAllTransactionSeriliazer
    queryset = TierOne.objects.all()

    def get(self, request):
        user = request.user
        transactions = self.queryset.filter(investor = user)
        serializer = self.serializer_class(instance=transactions, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

getTransactions = GetAllTransaction.as_view()

