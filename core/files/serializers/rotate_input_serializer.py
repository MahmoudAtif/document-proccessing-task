from rest_framework import serializers


class RotateInputSerializer(serializers.Serializer):
    angel = serializers.FloatField()