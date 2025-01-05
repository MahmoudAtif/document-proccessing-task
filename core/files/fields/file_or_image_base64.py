import filetype
from drf_extra_fields.fields import Base64FileField
from django.utils.translation import gettext_lazy as _


class Base64FileOrImageField(Base64FileField):
    ALLOWED_TYPES = ("pdf", "jpg", "jpeg", "png")

    INVALID_TYPE_MESSAGE = _(
        "Only files with extensions "
        f"{', '.join(ALLOWED_TYPES)} are allowed."
    )

    def get_file_extension(self, filename, decoded_file):
        extension = filetype.guess_extension(decoded_file)
        return extension
