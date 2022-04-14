import web
import app     
import pyrebase
import firebase_config as token
import json  
        
render = web.template.render("mvc/view/public", base="layout")
           
class Dash:
    def GET(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            db = firebase.database()
            return render.dash()
        except Exception as error:
            print("Error dash.GET: {}".format(error))