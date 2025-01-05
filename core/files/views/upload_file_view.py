from rest_framework import generics
from core.files.models import FileModel
from core.files.serializers import UploadFileModelSerializer


class FileUploadApi(generics.CreateAPIView):
    queryset = FileModel.objects.all()
    serializer_class = UploadFileModelSerializer
