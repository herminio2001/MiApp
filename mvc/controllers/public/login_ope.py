import web
import app     
import pyrebase
import firebase_config as token
import json  
        
render = web.template.render("mvc/view/public", base="layout")
           
class Login_ope:
    def GET(self):
        return render.login_ope()   