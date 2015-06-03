#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
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
        last_request = RequestRecognizer.objects.latest('id')
        return Response({'response': last_request.access})

    def post(self, request, format=None):
        serializer = RequestRecognizerSerializer(data=request.data)
        if serializer.is_valid():
            if not RequestRecognizer.objects.filter(
                    access=None,
                    result_recognizer__isnull=False,
            ): # If not exist a request recognizer - Singleton
                register = serializer.save()
                recognize_photo(register.id) # Run the recognizer task
                register = RequestRecognizer.objects.get(id=register.id)
                if register.result_recognizer is None:
                    return Response(
                        {'response': False, 'user': None}
                    )
                return Response(
                    {
                        'response': True,
                        'msm': 'Su solicitud esta siendo procesada ...',
                        'user': register.get_nombre_usuario_parameter,
                    },
                    status=status.HTTP_201_CREATED,
                )
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

    def get(self, request, format=None):
        request_rg = get_current_request()
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


@parser_classes((JSONParser,))
class RequestRecognizerResponse(APIView):
    """
    Response and update a RequestRecognizer instance.
    """

    def post(self, request, format=None):
        request_rg = get_current_request()
        if request_rg is None or not request_rg.access is None:
            #raise Http404
            return Response({'message': u'Ya se ha dado respuesta a esta petición'})
        if request.data.has_key('estado'):
            if request.data['estado'] == 'true':
                request_rg.access = True
            elif request.data['estado'] == 'false':
                request_rg.access = False
            request_rg.save()
            return Response({
                'transaction': u'true',
            })
        return Response(
            {'error': 'Opss that error!!'},
            status=status.HTTP_400_BAD_REQUEST,
        )


def get_current_request(code=None):
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
