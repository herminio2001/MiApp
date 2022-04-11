import web
import app     
import pyrebase
import firebase_config as token
import json  
        
render = web.template.render("mvc/view/public", base="layout")
           
class List_user_ope:
    def GET(self):
        return render.list_user_ope() 