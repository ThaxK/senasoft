import requests, uuid, json

#creacion de clase conexion
class ConexionTranlator:
    #diseño de variables location y key
    key = "6b3710a6b30e4cf2a066b494c0b3ab6a"
    endpoint = "https://api.cognitive.microsofttranslator.com"
    location = "eastus"
    path = '/translate'
    constructed_url = endpoint + path

    #diseño de parametros
    params = {
        'api-version': '3.0',
        'from': 'es',
        'to': ['fr', 'en','pt']
    }
    
    #diseño de headers
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    
