from PIL import Image
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from core.files.models import FileModel
from core.files.serializers import FileModelSerializer, RotateInputSerializer


class ImageApi(viewsets.ModelViewSet):
    queryset = FileModel.objects.exclude(extention="pdf")
    serializer_class = FileModelSerializer
    http_method_names = ["get", "delete", "post"]

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed(request)

    @action(methods=["POST"], detail=True)
    def rotate(self, *args, **kwargs):
        serializer = RotateInputSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        instance = self.get_object()
        img_path = instance.file.path

        with Image.open(img_path) as img:
            rotated_img = img.rotate(serializer.validated_data["angel"])
            rotated_img.save(img_path)

        return Response({"message": "Image rotated successfully"})
