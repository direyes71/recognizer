## Service camera ##
curl --form "image=@img.jpg" http://52.10.240.204:9000/recognize/

This web service requires a JSON data. Example

{image: @img.jpg}



## Services Android ##

# Get current request to recognize
curl -i -H "Accept: application/json" -H "Content-Type: application/json" http://52.10.240.204:9000/recognize/requests/

This web service returns a JSON data. Example

{"id":10,"image":"/media/images/img_n0weeTg.jpg","result_recognizer":"{u'confidence': 47, u'uid': u'harol', u'level': u'Medio'}","access":null}


# Post. Send response android to server
curl -X PUT -d access=True http://52.10.240.204:9000/recognize/requests/{id}/

{id} Register ID for access

This web service requires a JSON data. Example

{access: True}

The access parameter can be True or False



## NOTES ##

If you want see the current database register.

http://52.10.240.204:9000/recognize/
