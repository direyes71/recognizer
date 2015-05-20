#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'diego'

from rest_framework import serializers

from app.models import RequestRecognizer


class RequestRecognizerSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    IdPeticion = serializers.CharField(source='code', required=False)

    class Meta:
        model = RequestRecognizer
        fields = (
            'id',
            'image',
            'result_recognizer',
            'access',
            'IdPeticion',
            'bArrayImage',
        )
