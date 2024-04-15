from rest_framework import serializers
from api_clients.nasa_client import NasaCamerasChoices


class RetrieveMarsPhotosSerializer(serializers.Serializer):
    camera = serializers.ChoiceField(choices=NasaCamerasChoices.choices)
    earth_date = serializers.DateField()
    page_number = serializers.IntegerField(default=0)
