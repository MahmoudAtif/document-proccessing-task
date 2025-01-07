from PIL import Image
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from drf_spectacular.utils import extend_schema
from core.files.models import FileModel
from core.files.serializers import FileModelSerializer, RotateInputSerializer


class ImageApi(viewsets.ModelViewSet):
    queryset = FileModel.objects.exclude(extension="pdf")
    serializer_class = FileModelSerializer
    http_method_names = ["get", "delete", "post"]

    @extend_schema(exclude=True)
    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed(request)

    @extend_schema(request=RotateInputSerializer)
    @action(methods=["POST"], detail=True)
    def rotate(self, *args, **kwargs):
        serializer = RotateInputSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        instance = self.get_object()
        img_path = instance.file.path

        with Image.open(img_path) as img:
            rotated_img = img.rotate(serializer.validated_data["angle"])
            rotated_img.save(img_path)

        serializer = self.get_serializer(instance)

        return Response(
            {
                "message": "Image rotated successfully",
                "data": serializer.data,
            }
        )
