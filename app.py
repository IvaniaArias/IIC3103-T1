from flask import Flask, render_template, request
import requests
import urllib.request
import json

app = Flask(__name__)

link = "https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26322"


@app.route("/")
def index():
    
    #respuesta_url = requests.get(link)
    #respuesta_json = respuesta_url.text    #Respuesta que me dio el servidor, lo convierte a texto
    #dicc = json.loads(respuesta_json)       #pasa a json
    #print(data)
    return render_template('index.html') 

@app.route("/search", methods=['POST'])
def search():
    a_buscar = request.form["content"]
    
    #Usuarios
    url = link + f"/users/?name={a_buscar}"
    respuesta_url = requests.get(url)
    respuesta_url.raise_for_status()
    respuesta_json = respuesta_url.text
    datos = json.dumps(respuesta_json)

    #if respuesta_url.status_code != 204:
    #    print(respuesta_url.json())
    #    return respuesta_url.json()
 
    resultados_users = []

    #Ciudades
    url = link + f"/cities/?name={a_buscar}"
    respuesta_url = requests.get(url)
    respuesta_url.raise_for_status()
    respuesta_json = respuesta_url.text
    datos = json.dumps(respuesta_json)

    return render_template("search.html", users=resultados_users)

@app.route("/users/<int:id>")
def users(id):
    url = link + f"/users/{id}"
    respuesta_url = requests.get(url)
    respuesta_json = respuesta_url.text    #Respuesta que me dio el servidor, lo convierte a texto
    #dicc = json.loads(respuesta_json) 
    datos = json.dumps(respuesta_json)

    ids_users = []
    datos_users = []

    for user in datos['users']:
        user = int(user)
        ids_users.append(user)

    '''url2 = link + f"/users/{ids_users}"
    respuesta_url2 = requests.get(url2)
    respuesta_json2 = respuesta_url2.text    #Respuesta que me dio el servidor, lo convierte a texto
    #dicc = json.loads(respuesta_json) 
    datos_users = json.dumps(respuesta_json2)
    '''
    return render_template("users.html", user=datos)


@app.route("/cities/<int:id>")    #Tambien guarda la variable
def cities(id):
    url = link + f"cities/{id}"

    
    respuesta_url = requests.get(url)
    respuesta_json = respuesta_url.text    #Respuesta que me dio el servidor, lo convierte a texto
    #dicc = json.loads(respuesta_json)       #pasa ciudades a json
    respuesta_dicc = json.dumps(respuesta_json)
    '''

    id_users = list()
    info_users = dict()
    '''

    #return render_template("cities.html", cities=dicc, info_users=info_users)
    return render_template('cities.html')


if __name__ == "__main__":
    app.run(debug = True)
