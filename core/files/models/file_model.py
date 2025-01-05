from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator


class FileModel(models.Model):
    file = models.FileField(
        _("File"),
        upload_to="uploads/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["pdf", "jpg", "jpeg", "png"]
            )
        ],
    )
    extension = models.CharField(_("Extension"), max_length=10)
    width = models.FloatField(_("Width"), null=True, blank=True)
    height = models.FloatField(_("Height"), null=True, blank=True)
    number_of_channels = models.FloatField(
        _("Number of channels"), null=True, blank=True
    )
    number_of_pages = models.FloatField(
        _("Number of pages"), null=True, blank=True
    )

    class Meta:
        db_table = "files_filemodel"
        verbose_name = _("File Model")
        verbose_name_plural = _("Files Model")
