import web
import app     
import pyrebase
import firebase_config as token
import json  
        
render = web.template.render("mvc/view/public", base="layout")
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()
db = firebase.database()         

class Registrar:
    def GET(self):
        return render.registrar()

    def POST(self):
        try:
            formulario = web.input()
            nombre = formulario.nombre
            telefono = formulario.telefono
            email = formulario.email
            nivel = formulario.nivel
            estado = formulario.estado
            password = formulario.password
            print(email,password)
            #print(localID)
            #print("Registrado")
            user = auth.create_user_with_email_and_password(email, password)
            print("localId: ",user['localId'])
            data = {
                "nombre": nombre,
                "telefono": telefono,
                "email": email,
                "nivel":nivel, 
                "estado":estado
            }
            results = db.child("users").child(user['localId']).set(data)

            print(results)
            return render.registrar()
        except Exception as error:
            formato = json.loads(error.args[1]) # Error en formato JSON
            error = formato['error'] # Se obtiene el json de error
            message = error['message'] # se obtiene el mensaje de error
            print("Error Login.POST: {}".format(message))
            #if message == "EMAIL_NOT_FOUND":
            return render.correo_existe()
    