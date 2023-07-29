import flask

web_app = flask.Flask('miprimerweb')

# vamos a crea una funcion para cada ruta(pagina) de nuestra web
# una funcion diferente para cada ruta, ejemplo:
# queremos un sitio, con
# un home 
# una seccion acerca de nosotros 
# y otra para el tasador

def index():
   return 'Hola mundo! Bienvenidos a nuestra primer web en python!'

def about():
   return 'Somos estudiantes de coderhouse aprendiendo MLOps'

def modelo():
   return 'Proximamente nuestro modelo'

# agrego las rutas de nuestra web
web_app.add_url_rule('/', 'index', index)
web_app.add_url_rule('/nosotros/', 'about', about)
web_app.add_url_rule('/modelo/', 'modelo', modelo)


# finalmente ejecutamos el servidor-web
# python se encargara de enviar la informacion al cliente-web

web_app.run(port=3000)