'''
Created on 12-May-2018

@author: parthasarathy
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "KichRadu"

if __name__ == '__main__' :
    app.run(port=5000, debug = True)
    
    