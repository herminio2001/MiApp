import web
import app     
import pyrebase
import firebase_config as token
import json  
        
render = web.template.render("mvc/view/public", base="layout")
           
class Recuperar_con:
    def GET(self):
        return render.recuperar_con()