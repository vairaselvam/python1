from flask import Flask
import FaceAuth
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Vaira !!!"

@app.route("/face")
def face():
    imgkeys =  list(FaceAuth.face_train())
    print(imgkeys)
    return json.dumps({"name": imgkeys[-1], "length": len(imgkeys) }) 