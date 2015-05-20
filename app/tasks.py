__author__ = 'diego'

from django.conf import settings

from face_client import FaceClient

from app.data import DEACTIVE_STATUS
from app.data import LEVEL_RECOGNIZE_HIGH
from app.data import LEVEL_RECOGNIZE_MEDIUM
from app.models import RequestRecognizer


def recognize_photo(request_id):
    """
        This task execute the recognizer function
    """
    request = RequestRecognizer.objects.get(id=request_id)
    request.imagenByteArray = request.image_to_binary
    request.save()

    # Create one instance of library for connect to webservice
    client = FaceClient(
        '245c8bb50b2f42228a6a998863f5a1e0',
        'c1800f96cf0647fb8412ae8d3dae1202',
    )

    # Call function web service
    result = client.faces_recognize(
        'all',
        file=request.image,
        aggressive=True,
        namespace='CompareFaces',
    )

    # Validate if there are results
    if result['photos'][0]['tags']:
        recognize = None
        level_recognize = ''

        for item in result['photos'][0]['tags'][0]['uids']: # If exists coincidences
            if item['confidence'] >= 70:
                level_recognize = LEVEL_RECOGNIZE_HIGH
            elif item['confidence'] >= 40 and item['confidence'] < 70:
                level_recognize = LEVEL_RECOGNIZE_MEDIUM
            if not recognize and item['confidence'] < 40:
                request.access = False
                request.status = DEACTIVE_STATUS
            if not recognize or (recognize and item['confidence'] > recognize['confidence']):
                recognize = item
                recognize['uid'] = recognize['uid'].split('@')[0]
                recognize['level'] = level_recognize
        request.result_recognizer = recognize
        request.save()
