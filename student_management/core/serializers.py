from rest_framework import serializers
from core import models as core_models
from core import constants as core_constants



class CollageSerializer(serializers.Serializer):
    collage_name = serializers.CharField(max_length = 20)
    code = serializers.CharField(max_length = 20)
    collages_type = serializers.ChoiceField(
            choices = core_constants.COLLAGE_CHOICE)
    city = serializers.CharField(max_length = 20)

    def validate_collage_name( self , value):
        collage_instance = core_models.Collages.objects.filter(collage_name = value).last()
        if collage_instance:
            raise serializers.ValidationError("collage already exist")
        return value    