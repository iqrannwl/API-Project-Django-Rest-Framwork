from rest_framework import serializers
from .models import *

class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields='__all__'

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model=Projects
        fields='__all__'

class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Videos
        fields='__all__'

class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields='__all__'        
                