## Service camera ##
curl --form "image=@img.jpg" http://52.10.240.204:9000/recognize/

This web service requires a JSON data. Example

{image: @img.jpg}



## Services Android ##

# Get current request to recognize
curl -i -H "Accept: application/json" -H "Content-Type: application/json" http://52.10.240.204:9000/recognize/requests/


# Post. Send response android to server
curl -X PUT -d access=True http://52.10.240.204:9000/recognize/requests/{id}/

{id} Register ID for access

This web service requires a JSON data. Example

{access: True}

The access parameter can be True or False
