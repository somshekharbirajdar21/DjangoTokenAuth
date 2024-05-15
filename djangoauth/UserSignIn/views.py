from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .UserSerializers import UserSignInSerializer

# Create your views here.
@api_view(['POST'])
def signInView(request):
    serializer = UserSignInSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
