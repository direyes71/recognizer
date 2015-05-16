__author__ = 'diego'

from django.forms import ModelForm

from app.models import RequestRecognizer


class RequestRecognizerForm(ModelForm):

    class Meta:
        model = RequestRecognizer
        fields = ['image']