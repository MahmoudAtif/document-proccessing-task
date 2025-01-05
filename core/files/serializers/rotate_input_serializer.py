from rest_framework import serializers


class RotateInputSerializer(serializers.Serializer):
    angle = serializers.FloatField()