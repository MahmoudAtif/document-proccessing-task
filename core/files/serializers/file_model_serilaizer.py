from rest_framework import serializers
from core.files.models import FileModel


class FileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = [
            "id",
            "file",
            "extention",
            "width",
            "height",
            "number_of_channels",
            "number_of_pages",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if representation["extention"] == "pdf":
            representation.pop("number_of_channels")
        else:
            representation.pop("number_of_pages")

        return representation
