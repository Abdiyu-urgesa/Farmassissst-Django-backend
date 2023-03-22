from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from ..serializers import *
from ..models import *

@api_view(['GET'])
def getZones(request):
    zones = Zone.objects.all()
    serializer = ZoneSerializer(zones, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createZone(request):
    data = request.data
    try:
        user= User.objects.create_user(username=data['username'],email=data['email'] ,password=data['password'])
        region=Region.objects.get(id=data['created_by'])
        my_group = Group.objects.get(name='zone')
        my_group.user_set.add(user)
        if user and region:
            zone = Zone.objects.create(
                user=user,
                Zone_name=data['Zone_name'],
                created_by=region
              )
            serializer = ZoneSerializer(zone, many=False)
            return Response(serializer.data)
        else:
            return Response("user creation failed")   
           
    except:
        return Response("something went wrong in the try block") 
        
@api_view(['GET'])
def getZone(request, pk):
    try:
        zone = Zone.objects.get(id=pk)
        serializer = ZoneSerializer(zone, many=False)
        return Response(serializer.data)
    except:
        return Response("user not found")


@api_view(['PUT'])
def updatZone(request, pk):
    data = request.data
    zone = Zone.objects.get(id=pk)
    serializer = ZoneSerializer(instance=zone, data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

