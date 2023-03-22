from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from ..serializers import *
from ..models import *

@api_view(['GET'])
def getFederals(request):
    federals = Federal.objects.all()
    serializer = FederalSerializer(federals, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createFederal(request):
    data = request.data
    try:
        user= User.objects.create_user(username=data['username'],email=data['email'] ,password=data['password'])
        my_group = Group.objects.get(name='federal')
        my_group.user_set.add(user)
        if user:
            federal = Federal.objects.create(
                user=user,
                Federal_name=data['Federal_name'],
              )
            serializer = FederalSerializer(federal, many=False)
            return Response(serializer.data)
        else:
            return Response("user creation failed")   
           
    except:
        return Response("something went wrong in the try block") 
        
@api_view(['GET'])
def getFederal(request, pk):
    try:
        federal = Federal.objects.get(id=pk)
        serializer = FederalSerializer(federal, many=False)
        return Response(serializer.data)
    except:
        return Response("user not found")


@api_view(['PUT'])
def updatFederal(request, pk):
    data = request.data
    createFederal = Federal.objects.get(id=pk)
    serializer = FederalSerializer(instance=createFederal, data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

