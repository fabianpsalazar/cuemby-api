from rest_framework import serializers

class PlayerSerializers(serializers.Serializer):
    '''Serialize a field to prove our API view '''
    name = serializers.CharField(max_length=100)
    position = serializers.CharField(max_length=5)
    nation = serializers.CharField(max_length=100)
    club = serializers.CharField(max_length=100)

class TeamSerializers(serializers.Serializer):
    club = serializers.CharField(max_length=100)

class ClubSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    position = serializers.CharField(max_length=5)
    nation = serializers.CharField(max_length=100)
