from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import FileUploadApi, ImageApi, PdfApi

router = DefaultRouter()
router.register("images", ImageApi, basename="images")
router.register("pdfs", PdfApi, basename="pdfs")

urlpatterns = [path("upload/", FileUploadApi.as_view(), name="upload")]

urlpatterns += router.urls
