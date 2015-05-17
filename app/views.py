#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import RequestRecognizer
from app.serializers import RequestRecognizerSerializer
from tasks import recognize_photo

# Create your views/webServices here.


class RequestRecognizerList(APIView):
    """
    List all requests, or create a new request.
    """
    def get(self, request, format=None):
        requests_rg = RequestRecognizer.objects.all()
        serializer = RequestRecognizerSerializer(requests_rg, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RequestRecognizerSerializer(data=request.data)
        if serializer.is_valid():
            if not RequestRecognizer.objects.filter(access=None): # If not exist a request recognizer - Singleton
                register = serializer.save()
                recognize_photo(register.id) # Run the recognizer task
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {'message': u'Ya existe una petición de acceso en progreso'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
