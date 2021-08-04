from django.shortcuts import render
from rest_framework import response
from rest_framework.utils import serializer_helpers
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from rest_framework import serializers, status
from . import serializers


class Fifa_api(APIView):

    serializer_class = serializers.TeamSerializers

    def get(self,request, format=None):
        an_apiview = [

        ]
        return Response({
            'Page':'',
            'totalPages':'',
            'Items':'',
            'totalItems':'',
            'Players': [{
                'name':'',
                'position':'',
                'nation':'',
                'team':'',
            }]
            
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            team_name = serializer.validated_data.get('team_name')
            page = serializer.validated_data.get('page')
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )