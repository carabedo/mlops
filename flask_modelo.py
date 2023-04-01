
from joblib import load
import pandas as pd


modelo, prepro = load('modelo.joblib') 

def pipeline(tipo,barrio,sup,habs):
    X_pred=pd.DataFrame(columns=['tipo','barrio','sup','habs'])
    X_pred.loc[0,:]=[tipo,barrio,sup,habs]
    X_pred_dummies=prepro.transform(X_pred)    
    return modelo.predict(X_pred_dummies)[0]

# el modelo ya esta importado y listo

# creamos la API
from flask import Flask, jsonify, request

web_app = Flask('miprimerweb')

# primero vamos a crear una funcion para cada ruta(pagina) de nuestra web
# una funcion diferente para cada ruta, ejemplo:
# queremos un sitio, con
# un home 
# una seccion acerca de nosotros 
# y otra para el tasador

def index():
    return '<h1 style="color:blue">Hola mundo! Bienvenidos a nuestra primer web en python!</h1>'

def about():
    return 'Somos estudiantes de coderhouse aprendiendo MLOps'

def deploy_modelo():
    data = request.get_json(force=True)
    print(data)
    try:
        tipo = data['tipo']
        barrio = data['barrio']
        sup = int(data['sup'])
        habs = int(data['habs'])
        print('si')
        pred=pipeline(tipo,barrio,sup,habs)
        resp={'response' : pred}
    except Exception as e:
        resp={'response' : str(e)}

    return jsonify(resp)


# agrego las rutas de nuestra web
web_app.add_url_rule('/', 'index', index)
web_app.add_url_rule('/nosotros/', 'about', about)
web_app.add_url_rule('/modelo/', 'modelo', deploy_modelo, methods=['POST'])


# finalmente ejecutamos el servidor-web
# python se encargara de enviar la informacion al cliente-web

web_app.run(host='0.0.0.0',debug=True,port=3000)