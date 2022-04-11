import web
import app     
import pyrebase
import firebase_config as token
import json  
        
render = web.template.render("mvc/view/public", base="layout")
           
class Login:
    def GET(self):
        return render.login()
        try:
            return render.login()
        except Exception as error:
            print("Error Login.GET: {}".format(error.args[0]))
    def POST(self):  
        formulario = web.input()
        email = formulario.email
        password = formulario.password
        #user = auth.sign_in_with_email_and_password(email, password)
        #print(user['localId'])
        #return render.login()              
        try:
            formulario = web.input()
            email = formulario.email
            password = formulario.password
            user = auth.sign_in_with_email_and_password(email, password)
            print(user['localId'])

            #informacion = auth.get_account_info(user['idToken'])
            #usuarios = informacion['users']
            #usuario = usuarios[0]
            #localid = usuario['localId']
            #web.setcookie('localid', localId)

            web.setcookie('localID', user['localId']) # se almacena en una cookie el localID
            print("localId : ",web.cookies().get('localID'))

            #message = "Bienvenido"
            #return render.login(message)
            return render.bienvenida()
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
                #message1 = "contraseña incorrecta"
            #return render.login(message1)
            #print(error['message'])
            #return render.login()   