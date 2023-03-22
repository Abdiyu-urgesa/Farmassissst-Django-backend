from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from ..serializers import *
from ..models import *

@api_view(['GET'])
def getRegions(request):
    regions = Region.objects.all()
    serializer = RegionSerializer(regions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createRegion(request):
    data = request.data
    try:
        user= User.objects.create_user(username=data['username'],email=data['email'] ,password=data['password'])
        federal=Federal.objects.get(id=data['created_by'])
        my_group = Group.objects.get(name='region')
        my_group.user_set.add(user)
        if user and federal:
            region = Region.objects.create(
                user=user,
                region_name=data['region_name'],
                created_by=federal
              )
            serializer = RegionSerializer(region, many=False)
            return Response(serializer.data)
        else:
            return Response("user creation failed")   
           
    except:
        return Response("something went wrong in the try block") 
        
@api_view(['GET'])
def getRegion(request, pk):
    try:
        region = Region.objects.get(id=pk)
        serializer = RegionSerializer(region, many=False)
        return Response(serializer.data)
    except:
        return Response("user not found")


@api_view(['PUT'])
def updatRegion(request, pk):
    data = request.data
    region = Region.objects.get(id=pk)
    serializer = RegionSerializer(instance=region, data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

