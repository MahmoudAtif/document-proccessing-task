from rest_framework import serializers
from core.files.models import FileModel


class FileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = [
            "id",
            "file",
            "extension",
            "width",
            "height",
            "number_of_channels",
            "number_of_pages",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if representation["extension"] == "pdf":
            representation.pop("number_of_channels")
        else:
            representation.pop("number_of_pages")

        return representation
