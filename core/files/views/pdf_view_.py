import os
from PIL import Image
from pdf2image import convert_from_path
from django.core.files.storage import FileSystemStorage
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.decorators import action
from core.files.models import FileModel
from core.files.serializers import FileModelSerializer


class PdfApi(viewsets.ModelViewSet):
    queryset = FileModel.objects.filter(extention="pdf")
    serializer_class = FileModelSerializer
    http_method_names = ["get", "delete", "post"]

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed(request)

    @action(methods=["POST"], detail=True, url_path="convert-pdf-to-image")
    def convert_pdf_to_image(self, *args, **kwargs):
        instance = self.get_object()
        try:
            images = convert_from_path(instance.file.path)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )
        
        files_to_be_create = []

        for page_num, image in enumerate(images, start=1):
            file_name = f"converted_from_pdf_{instance.id}_{page_num}.png"
            file_system_storage = FileSystemStorage(location="media/uploads/")
            file_path = os.path.join(file_system_storage.location, file_name)
            image.save(file_path)

            with Image.open(file_path) as img:
                number_of_channels = len(img.getbands())

            files_to_be_create.append(
                FileModel(
                    file=f"uploads/{file_name}",
                    width=image.width,
                    height=image.height,
                    number_of_channels=number_of_channels,
                )
            )
        FileModel.objects.bulk_create(files_to_be_create)
        instance.delete()
        return Response({"message": "success"})
