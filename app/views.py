#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
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
                register = RequestRecognizer.objects.get(id=register.id)
                serializer = RequestRecognizerSerializer(register)
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
    def get_object(self, code=None):
        """
            Only return the current request for recognizer
        """
        if code:
            return get_object_or_404(RequestRecognizer, code=code)
        # Validate that the register was processed:
        # result_recognizer should be different of None
        request_rg = RequestRecognizer.objects.filter(
            access__isnull=True,
            result_recognizer__isnull=False,
            status=ACTIVE_STATUS,
        )
        if request_rg:
            return request_rg[0]
        return None

    def get(self, request, format=None):
        request_rg = self.get_object()
        if request_rg is None:
            #return Response({'message': u'No hay peticiones pendientes'})
            # Return empty JSON
            return Response({
                'estado': u'false',
                'idPeticion': '00000000-0000-0000-0000-000000000000',
                'imagenByteArray': '',
                'nombreUsuario': '',
            })
        serializer = RequestRecognizerSerializer(request_rg)
        return Response(serializer.data)

    def put(self, request, format=None):
        request_rg = self.get_object()
        if request_rg is None or not request_rg.access is None:
            #raise Http404
            return Response({'message': u'Ya se ha dado respuesta a esta petición'})
        serializer = RequestRecognizerSerializer(request_rg, data=request.data)
        if serializer.is_valid():
            rq = serializer.save()
            if serializer.data['estado'] == 'true':
                rq.access = True
            elif serializer.data['estado'] == 'false':
                rq.access = False
            rq.save()
            return Response({
                'transaction': u'true',
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
