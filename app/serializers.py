#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'diego'

from rest_framework import serializers

from app.models import RequestRecognizer


class RequestRecognizerSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    idPeticion = serializers.CharField(source='code', required=False)

    # parse "nombreUsuario" person that was recognized for Android
    nombreUsuario = serializers.CharField(
        source='get_nombre_usuario_parameter',
        required=False,
    )

    # parse "estado" person that was recognized for Android
    estado = serializers.CharField(
        source='get_estado_parameter',
        required=False,
    )

    class Meta:
        model = RequestRecognizer
        fields = (
            'id',
            'image',
            'result_recognizer',
            'access',
            'idPeticion',
            'nombreUsuario',
            'estado',
            'imagenByteArray',
        )
