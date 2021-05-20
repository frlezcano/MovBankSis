import requests
import json

url="http://192.168.129.171:9003/api/simeac-backend/auth/login"
_json= {"password" : "dos01", "username" : "jmaubet"}
_headers= {'accept': 'application/json', 'system': 'sirec', 'Content-Type': 'application/json'}
_response=None
try:
    _response=requests.post(url, data=json.dumps(_json), headers=_headers, timeout=1.5)
except requests.Timeout:
    pass
except requests.ConnectionError:
    pass

print("-------------Inicio de sesión-------------")

if (_response is not None):
    dataJson=_response.json()
    print(dataJson)
    print("------------------------------------------")
    # response
    _tiempo     = dataJson['timestamp']
    _status     = dataJson['status']

    # lee message
    _descripcion= dataJson['message']['messages'][0]['description']

    if (_status==200):
        # lee data
        _usuario    = dataJson['data']['username']
        _nombre     = dataJson['data']['name']
        _apellido   = dataJson['data']['lastname']
        _dependencia= dataJson['data']['dependency']
        _idsesion   = dataJson['data']['session_id']
        if (_descripcion=='ACCESO CONFIRMADO'):
            print("ACCESO CONFIRMADO")
            print("Tiempo     : "+_tiempo)
            print("Dependencia: "+_dependencia)
            print("Nombre     : "+_nombre + " " + _apellido) 
        else:            
            print("ACCESO DENEGADO")
            print("Tiempo       : "+_tiempo)
    else:
        print("ACCESO DENEGADO")
        print("Tiempo       : "+_tiempo)
        print(_descripcion)
else:
    print("ERROR DE CONEXION CON EL SERVIDOR DE ACCESO")

