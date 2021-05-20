import requests
import json

url="http://192.168.129.171:9003/api/simeac-backend/auth/login"
_json= {"password" : "dos01", "username" : "jmaubet"}
_headers= {'accept': 'application/json', 'system': 'sirec', 'Content-Type': 'application/json'}

response=requests.post(url, data=json.dumps(_json), headers=_headers)

dataJson=response.json()

print(response)
print(response.url)
print(response.content)
print(" ")
print("Indentificación")
print("---------------")
print(type(dataJson))
print(dataJson)
print("Estado      : "+type(dataJson['message']['messages']['description']))
print("Usuario   : "+dataJson['data']['username'])
# print("Nombre    : "+dataJson['name'] + " " + dataJson['lastname'])

print("Tiempo      : "+dataJson['timestamp'])

#Valor numerico (convertir a string)
#print("Status      : "+dataJson['status'])

#def print_properties(value, parent):
#    if type(value) is dict:
#        for (key, val) in value.items():
#            if type(val) is dict:
#                print_properties(val, parent + '.' + key)
#            else:
#                print("{}: {}".format(parent + '.' + key, val))
#    else:
#        print("{}: {}".format(parent, value))


#for (key, val) in json.items():
#    print_properties(val, key)
