from backend.models import Musician
from rest_framework import serializers

class MusicianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Musician
        fields = (
            'id',
            'first_name',
            'last_name',
            'instrument'
        )