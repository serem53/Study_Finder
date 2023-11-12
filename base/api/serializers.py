from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializer(ModelSerializer):
    """ Serializer for the room model """
    class Meta:
        model = Room
        fields = '__all__'
        