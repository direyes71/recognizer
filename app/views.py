#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.data import ACTIVE_STATUS
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


class RequestRecognizerDetail(APIView):
    """
    Retrieve and update a RequestRecognizer instance.
    """
    def get_object(self, pk=None):
        """
            Only return the current request for recognizer
        """
        if pk:
            return get_object_or_404(RequestRecognizer, pk=pk)
        # Validate that the register was processed:
        # result_recognizer should be different of None
        request_rg = RequestRecognizer.objects.filter(
            access=None,
            result_recognizer__isnull=False,
            status=ACTIVE_STATUS,
        )
        if request_rg:
            return request_rg[0]
        return None

    def get(self, request, pk=None, format=None):
        request_rg = self.get_object(pk)
        if request_rg is None:
            return Response({'message': u'No hay peticiones pendientes'})
        serializer = RequestRecognizerSerializer(request_rg)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        request_rg = self.get_object(pk)
        if not request_rg.access is None:
            #raise Http404
            return Response({'message': u'Ya se ha dado respuesta a esta petición'})
        serializer = RequestRecognizerSerializer(request_rg, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
