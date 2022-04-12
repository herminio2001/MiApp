import web
import app     
import pyrebase
import firebase_config as token
import json  

firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()
db = firebase.database()     
render = web.template.render("mvc/view/public", base="layout")
           
class Login_ope:
    def GET(self):
        return render.login_ope()   
    def POST(self):
        formulario = web.input()
        email = formulario.email
        password = formulario.password          
        try:
            formulario = web.input()
            email = formulario.email
            password = formulario.password
            user = auth.sign_in_with_email_and_password(email, password)
            print(user['localId'])

            web.setcookie('localID', user['localId']) # se almacena en una cookie el localID
            print("localId : ",web.cookies().get('localID'))

            return render.principal_ope()
        except Exception as error:
            formato = json.loads(error.args[1]) # Error en formato JSON
            error = formato['error'] # Se obtiene el json de error
            message = error['message'] # se obtiene el mensaje de error
            print("Error Login.POST: {}".format(message))
            if message == "EMAIL_NOT_FOUND":
                return render.error_email()
                #message1 = "Correo incorrecto"
            else:
                return render.error_cont()