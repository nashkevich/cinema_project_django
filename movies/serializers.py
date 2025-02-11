from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, JSONField, IntegerField

class MovieSerializer(serializers.ModelSerializer):
    title = CharField()
    year = IntegerField()
    class Meta:
        model = models.Movie
        fields = (
            'title',
            'year',
            'description',
            'poster',
            'cast',
            'genres'
        )

    def validate_year(self, value):
        if value > 2025:
            raise serializers.ValidationError("Year cannot be in the future.")
        return value