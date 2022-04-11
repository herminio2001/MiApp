import web
import app     
import pyrebase
import firebase_config as token
import json  


render = web.template.render("mvc/view/public", base="layout")
           
class Recuperar_con:
    def GET(self):
        return render.recuperar_con()

    def POST(self):
        firebase = pyrebase.initialize_app(token.firebaseConfig)
        auth = firebase.auth()
        formulario = web.input()
        email = formulario.email
        user = auth.send_password_reset_email(email)
        return render.recuperar_con() 