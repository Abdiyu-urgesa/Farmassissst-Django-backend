from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    return Response("farmassis backend")


@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response('user was deleted')

