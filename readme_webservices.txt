## TECHNICAL MANUAL ##


## Services camera ##


+ curl --form "image=@img.jpg" http://52.25.109.66:9000/recognize/

  This web service requires a JSON data. Example

  {image: @img.jpg}


+ curl -i -H "Accept: application/json" -H "Content-Type: application/json" http://52.25.109.66:9000/recognize/

  This web service returns a JSON with the answer sended from android

  {"response":false}


## Services Android ##


# Get current request to recognize

+ curl -i -H "Accept: application/json" -H "Content-Type: application/json" http://52.25.109.66:9000/recognize/requests/

  This web service returns a JSON data. Example

  {
        "nombreUsuario":"",
        "estado":"false",
        "idPeticion":"00000000-0000-0000-0000-000000000000",
        "imagenByteArray":""
  }


# Post. Send response from android to server

+ curl -X POST -d access=True http://52.25.109.66:9000/recognize/requests/response/

  This web service requires a JSON data. Example

  {estado: True}

  The access parameter can be True or False



## NOTES ##

If you want see the database register and details. From a browser go to next url

+ http://52.25.109.66:9000/admin/
