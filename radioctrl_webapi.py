# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
# クロスドメイン用
# sudo pip3 install -U flask-cors
from flask_cors import CORS

app = Flask(__name__)
#クロスドメイン用
CORS(app)


returnValue = "NA"
returnPosition = "NA"
nowAuto = False

# グロバル変数
val_label = "NA"

# コマンド返信
@app.route('/getcommand', methods=['GET'])
def getCommand():
    global returnValue
    global nowAuto
    returnValueNow = ""
    if nowAuto :
        returnValue = "Auto"
        return returnValue
    else :
        returnValueNow = returnValue
        returnValue = "NA"
        return returnValueNow
       

@app.route('/auto', methods=['PUT'])
def goAuto():
    global returnValue
    returnValue = "Auto"
    try:
        return returnValue
    except:
        return 'NG'

@app.route('/gostrate', methods=['PUT'])
def goStrate():
    global returnValue
    returnValue = "Strate"
    try:
        return returnValue
    except:
        return 'NG'

@app.route('/turnleft', methods=['PUT'])
def goLeft():
    global returnValue
    returnValue = "Left"
    try:
        return returnValue
    except:
        return 'NA'

@app.route('/turnright', methods=['PUT'])
def goRigth():
    global returnValue
    returnValue = "Right"
    try:
        return returnValue
    except:
        return 'NA'

@app.route('/stop', methods=['PUT'])
def goStop():
    global returnValue
    global nowAuto
    nowAuto = False
    returnValue = "Stop"
    try:
        return returnValue
    except:
        return 'NG'

@app.route('/', methods=['GET'])
def index():
    return render_template('radioctrl.html')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, use_reloader=True)