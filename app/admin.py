from django.contrib import admin

from app.models import RequestRecognizer

# Register your models here.


class RequestRecognizerAdmin(admin.ModelAdmin):
    fields = (
        'image',
        'status',
        'result_recognizer',
        'access',
        'code',
    )

admin.site.register(RequestRecognizer, RequestRecognizerAdmin)
