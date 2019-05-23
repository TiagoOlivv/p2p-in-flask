from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import socket
import random
import os
import string
import requests
import time

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
app.config['uploads'] = UPLOAD_FOLDER
hostname = socket.gethostname()

@app.route('/', methods = ['GET', 'POST'])
def upload():
    file = request.files['file']   
    filename = secure_filename(str(file))
    file.save(os.path.join(app.config['uploads'], filename[12:-5]))
    return 'ok'
# @app.route('/download', methods = ['GET', 'POST'])
# def download():
#     file = request.files['file']    
#     filename = secure_filename(str(file))
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename[12:-5]))

# @app.route('/', methods = ['GET'])
# def index():
#     file = request.files['file']   
#     filename = secure_filename(str(file))
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename[12:-5]))
	
#     return render_template('index.html')

if __name__ == '__main__':
   # app.run(debug = True, host = socket.gethostbyname(hostname),  port = 40000)
   app.run(debug = True, host = '192.168.43.208',  port = 5002)

