import web
import app     
import pyrebase
import firebase_config as token
import json  
        
render = web.template.render("mvc/view/public", base="layout")
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()
db = firebase.database()  
           
class List_user:
    def GET(self):
        #return render.list_user()  
        datos_usuarios = db.child("users").get()
        print(datos_usuarios)
        return render.list_user(datos_usuarios)  
        try:
            datos_usuarios = db.child("users").get()
            print(datos_usuarios)
            return render.list_user(datos_usuarios) 
        except Exception as error:
            return render.list_user(error) 