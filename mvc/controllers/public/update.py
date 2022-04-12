import web
import app     
import pyrebase
import firebase_config as token
import json 
import requests
import cgi

render = web.template.render("mvc/view/public", base="layout")
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()
db = firebase.database() 
class Update:

    def GET(self):
        
        #args = cgi.FieldStorage()
        #a = args['id'].value
        #print(a)
        #return render.update()
        #try:
         #   args = cgi.FieldStorage()
          #  a = args["id"].value
           # print(a)
            #return render.update()
        #except Exception as error:
         #   return render.update(error) 
        
        #a = requests.get(url = URL, params = "view")
          #  print(a)
            return render.update()
    def POST(self,localId):
        try:
            users= db.child("users").child(user['localId']).get() 
            formulario = web.input()
            nombre = formulario.nombre
            telefono = formulario.telefono
            email = formulario.email
            nivel = formulario.nivel
            estado = formulario.estado

            user = auth.update_user
            data = {'nombre': nombre,
                          'telefono': telefono,
                          'email':email, 
                          'nivel':nivel, 
                          'estado':estado
            } 
            result=db.child("up").child(nombre).update(data)         
            return web.seeother('/list_user') 
        except Exception as error:
            print("Error actualizar.POST: {}".format(error)) 
            return web.seeother('/list_user')