from rest_framework import serializers

class TeamSerializers(serializers.Serializer):
    '''Serialize a field to prove our API view '''
    team_name = serializers.CharField(max_length=100)
    page = serializers.IntegerField()