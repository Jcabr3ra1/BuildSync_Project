from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorInventario import ControladorInventario
from Controladores.ControladorMaterial import ControladorMaterial
from Controladores.ControladorProvedor import ControladorProvedor
from Controladores.ControladorProyecto import ControladorProyecto

app = Flask(__name__)
"""
Los cors permiten que se puedan hacer pruebas al
servidor desde las misma máquina donde está corriendo.
"""
cors = CORS(app)

miControladorInventario = ControladorInventario()
miControladorMaterial = ControladorMaterial()
miControladorProvedor = ControladorProvedor()
miControladorProyecto = ControladorProyecto()

#####################################Proyecto############################################################
@app.route("/Proyecto", methods=['GET'])
def getProyecto():
   json = miControladorProyecto.index()
   return jsonify(json)


@app.route("/Proyecto", methods=['POST'])
def crearProyecto():
   data = request.get_json()
   json = miControladorProyecto.create(data)
   return jsonify(json)


@app.route("/Proyecto/<string:id>", methods=['GET'])
def getProyecto(id):
   json = miControladorProyecto.show(id)
   return jsonify(json)


@app.route("/Proyecto/<string:id>", methods=['PUT'])
def modificarProyecto(id):
   data = request.get_json()
   json = miControladorProyecto.update(id, data)
   return jsonify(json)

@app.route("/Proyecto/<string:id>", methods=['DELETE'])
def eliminarProyecto(id):
   json = miControladorProyecto.delete(id)
   return jsonify(json)


#########################Servicios Provedor###################################
@app.route("/Provedor", methods=['GET'])
def getProvedor():
    json = miControladorProvedor.index()
    return jsonify(json)

@app.route("/Provedor/<string:id>", methods=['GET'])
def getProvedor(id):
    json = miControladorProvedor.show(id)
    return jsonify(json)

@app.route("/Provedor/<string:id>",methods=['DELETE'])
def eliminarProvedor(id):
    json = miControladorProvedor.delete(id)
    return jsonify(json)

#########################Servicios Material###################################
@app.route("/Material", methods=['GET'])
def getMaterial():
    json = miControladorMaterial.index()
    return jsonify(json)


@app.route("/Material", methods=['POST'])
def crearMaterial():
    data = request.get_json()
    json = miControladorMaterial.create(data)
    return jsonify(json)

@app.route("/Material/<string:id>", methods=['GET'])
def getMaterial(id):
    json = miControladorMaterial.show(id)
    return jsonify(json)

@app.route("/Material/<string:id>", methods=['PUT'])
def modificarMaterial(id):
    data = request.get_json()
    json = miControladorMaterial.update(id, data)
    return jsonify(json)


@app.route("/Material/<string:id>", methods=['DELETE'])
def eliminarMaterial(id):
    json = miControladorMaterial.delete(id)
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data
if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

