from django.db import models

from app.data import ACTIVE_STATUS
from app.data import STATUS_REGISTER


# Create your models here.


class RequestRecognizer(models.Model):
    date_register = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')
    status = models.PositiveSmallIntegerField(
        choices=STATUS_REGISTER,
        default=ACTIVE_STATUS,
    )