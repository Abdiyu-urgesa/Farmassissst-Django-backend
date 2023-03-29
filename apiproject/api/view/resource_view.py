from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from ..serializers import *
from ..models import *

@api_view(['GET'])
def getResources(request):
    resources = Resource.objects.all()
    serializer = ResourceSerializer(resources, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createResource(request):
    data = request.data
    try:
        resource = Resource.objects.create(
            name=data['name'],
            type=data['type'],
            amount=data['amount'],
            price_perKilo=data['price_perKilo']
        )       
        serializer = ResourceSerializer(resource, many=False)
        return Response(serializer.data)
    
    except:
        return Response("something went wrong in the try block") 
        


@api_view(['GET'])
def getResource(request, pk):
    try:
        resource = Resource.objects.get(id=pk)
        serializer = ResourceSerializer(resource, many=False)
        return Response(serializer.data)
    except:
        return Response("resource not found!!!")


@api_view(['PUT'])
def updateResource(request, pk):
    data = request.data
    resource = Resource.objects.get(id=pk)
    serializer = ResourceSerializer(instance=resource, data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    
    return Response(serializer.data)


@api_view(['GET'])
def transferResource(request):
    data = request.data
    resources = User.objects.get(id=1).resource_set.all()
    recserializer = ResourceSerializer(resources, many=True)
    return Response(recserializer.data)

