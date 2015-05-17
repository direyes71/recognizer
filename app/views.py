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
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = RequestRecognizer.objects.all()
        serializer = RequestRecognizerSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RequestRecognizerSerializer(data=request.data)
        if serializer.is_valid():
            register = serializer.save()
            recognize_photo(register.id) # Run the recognizer task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
