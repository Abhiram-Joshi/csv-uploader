from rest_framework import serializers

class CSVSerializer(serializers.Serializer):
    file = serializers.FileField()