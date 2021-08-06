from copy import error
from re import T
from django.http.response import HttpResponseBadRequest
from django.shortcuts import render
from rest_framework import response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from .models import Players
from rest_framework.permissions import IsAuthenticated
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

class Fifa_get(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PlayerSerializers

    def get_players(self,player, ord='asc'):
        if ord == 'desc':
            players = Players.objects.filter(name__icontains=player).order_by('-name')
            return players
        players = Players.objects.filter(name__icontains=player).order_by('name')
        return players

    def get(self, request, *args, **kwargs):

        try:
            search = request.query_params['search']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        try:
            order = request.query_params['order'].lower()
        except:
            order = 'asc'
                    
        players = self.get_players(search, order)
        serializer = serializers.PlayerSerializers(players, many=True)

        return Response({
            'Player': serializer.data,

            })

class Fifa_post(APIView):

    permission_classes = (IsAuthenticated,)

    serializer_class = serializers.TeamSerializers
        
    def get(self, request, format=None):

        return Response({
            'Message': 'Hello! Enter your team.'
        })

    def get_team(self, team_name, page=1):

        team_players = Players.objects.filter(club__iexact=team_name) #add here page filter
        return team_players

    def post(self, request):

        serializer = serializers.TeamSerializers(data=request.data)
        if serializer.is_valid():
            team = serializer.validated_data.get('club')
            team_players = self.get_team(team)
            players_serializer = serializers.ClubSerializers(team_players, many=True)    

            if players_serializer.data :
                return Response({
                    'players': players_serializer.data,
                })
            else:
                return Response({
                    'Message': 'Empty query'
                })
        else:
            return Response({
                'error': 'Bad input'
            })