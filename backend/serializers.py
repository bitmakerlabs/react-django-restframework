from backend.models import Musician, Album
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = (
            'artist',
            'name',
            'release_date',
            'num_stars'
        )

class MusicianSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True)

    class Meta:
        model = Musician
        fields = (
            'id',
            'first_name',
            'last_name',
            'instrument',
            'albums'
        )