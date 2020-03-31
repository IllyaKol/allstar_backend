import base64
from django.conf import settings


def encode_image(image_path):
    with open(f'{settings.MEDIA_ROOT}/{image_path}', 'rb') as img:
        return base64.b64encode(img.read())
