from django.core.files import File
from pathlib import Path
from PIL import Image
from io import BytesIO


image_types = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
    "tif": "TIFF",
    "tiff": "TIFF",
}


def image_resize(image, width, height):
    img = Image.open(image)

    if img.height > height or img.width > width:
        output_size = (width, height)
        img.thumbnail(output_size)
        img_filename =  Path(image.file.name).name
        img_suffix = Path(image.file.name).name.split(".")[-1]
        img_format = image_types[img_suffix]
        buffer = BytesIO()
        img.save(buffer, format=img_format)
        file_object = File(buffer)
        image.save(img_filename, file_object)