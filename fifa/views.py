from copy import error
from re import T
from django.http.response import HttpResponseBadRequest
from django.shortcuts import render
from rest_framework import response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
''' code HTTP status as responses'''
from rest_framework import status
from . import serializers
from .models import Players, Teams
'''To run pending to execute the virtual env'''
import requests
import json


def save_players():
    for j in range(1,909):
        fifa_url = f'https://www.easports.com/fifa/ultimate-team/api/fut/item?page={j}'
        response = requests.get(fifa_url).json()
        for i in response["items"]:
            players = Players()
            players.name = i["name"]
            players.nation = i["nation"]["name"]
            players.club = i["club"]["name"]
            players.position = i["position"]
            try:
                players.save()
            except:
                continue

#save_players()
# Create your views here.
class Fifa_get(APIView):
    '''Class of API view'''
    serializer_class = serializers.TeamSerializers


    def get_query(self,player, ord):
        players = Players.objects.filter(name__icontains=player).order_by('name')
        return players
    '''This set our API view to have the serializer class'''
    #Each function must return a response object
    def get(self, request, *args, **kwargs):

        try:
            search = request.query_params['search']
            page = int(request.query_params['page'])
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        try:
            order = request.query_params['order'].lower()
        except:
            order = 'asc'
            
        players = self.get_query(search, order)
        serializer = serializers.TeamSerializers(players, many=True)
        #Response transform the information to JSON, this information
        #must be an array or a dict
        return Response({
            'Player': serializer.data,

            })
        '''Now we can create a URL to view this api view through URL'''

class Fifa_post(APIView):

    def post(self, request, *args, **kwargs):
        '''Create a message with our name'''
        #Self.serializer is a class that set out class with the API view, standart method
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            '''This datas must be validated'''
            name = serializer.validated_data.get('team_name')
            page = serializer.validate_data.get('page')
            
            message = f'Hello {name}'
            return Response({
                'message': message
            })
        #Not valid information
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )