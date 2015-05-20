#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
import uuid

from jsonfield import JSONField

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
    result_recognizer = JSONField(null=True, default=None)
    access = models.NullBooleanField(null=True, default=None)
    code = models.CharField(max_length=50)
    bArrayImage = JSONField(null=True, default=None)

    @property
    def image_to_binary(self):
        with open(self.image.path, "rb") as f:
            bin_data = list(bytearray(f.read()))
            return bin_data

    @property
    def get_nombre_usuario_parameter(self):
        """
            This function is for parse "nombreUsuario" person that was recognized
            for Android
        """
        return self.result_recognizer['uid']

    def save(self, *args, **kwargs):
        # Create the IdPeticion field
        self.code = uuid.uuid4()
        super(RequestRecognizer, self).save(*args, **kwargs)
