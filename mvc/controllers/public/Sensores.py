import web
import app
import pyrebase
import firebase_config as token
import json


class Sensores:
    def GET(self):
        firebase = pyrebase.initialize_app(token.firebaseConfig) #Se inicializa la configuracion del firebase
        db = firebase.database()
        Sensores = db.child("sensores").get()
        result = json.dumps(Sensores.val())
        return result