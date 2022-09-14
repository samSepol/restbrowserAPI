from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CoderSerializer
from .models import Coder 
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from api import serializers
# Create your views here.


# using function based api view 

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def coder_API(request,id=None):
    if request.method =='GET':
        # get the data for specific id 
        id=id
        if id is not None:
            coder = Coder.objects.get(id=id)
            serializer=CoderSerializer(coder)
            return Response(serializer.data)

        # get all data
        coder=Coder.objects.all()
        serializer=CoderSerializer(coder,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method=='POST':
        serializer=CoderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data saved successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    # put request  

    if request.method=='PUT':
        id=request.data.get('id')
        coder=Coder.objects.get(id=id)
        serializer=CoderSerializer(coder,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data updated successfully !'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

       # PATCH partial update

    if request.method=='PATCH':
        id=request.data.get('id')
        coder=Coder.objects.get(id=id)
        serializer=CoderSerializer(coder,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data updated '})
        return Response(serializer.errors)


    if request.method=='DELETE':
        id=request.data.get('id')
        coder=Coder.objects.get(id=id)
        coder.delete()
        return Response({'msg':'Data deleted successfully !'})