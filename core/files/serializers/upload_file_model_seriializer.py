from PIL import Image
from PyPDF2 import PdfReader
from rest_framework import serializers
from core.files.models import FileModel
from core.files.fields import Base64FileOrImageField


class UploadFileModelSerializer(serializers.ModelSerializer):
    file = Base64FileOrImageField()

    class Meta:
        model = FileModel
        fields = ["id", "file"]

    def save(self, **kwargs):
        file = self.validated_data["file"]
        file_extension = file.name.split(".")[-1]
        self.validated_data["extention"] = file_extension
        number_of_channels = None
        number_of_pages = None

        if file_extension == "pdf":
            pdf = PdfReader(file)
            first_page = pdf.pages[0]
            width = first_page.mediabox.width
            height = first_page.mediabox.height
            number_of_pages = len(pdf.pages)
        else:
            with Image.open(file) as img:
                width = img.width
                height = img.height
                number_of_channels = len(img.getbands())

        self.validated_data["width"] = width
        self.validated_data["height"] = height
        self.validated_data["number_of_channels"] = number_of_channels
        self.validated_data["number_of_pages"] = number_of_pages
        instance = super().save(**kwargs)
        return instance
