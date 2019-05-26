import os, json
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import requests
import socket
import time

hostname = socket.gethostname()
UPLOAD_FOLDER = 'uploads'
app = Flask(__name__)
app.config['uploads'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload():
    file = request.files['file']
    filename = secure_filename(str(file))
    file.save(os.path.join(app.config[UPLOAD_FOLDER], filename[12:-5])) 
    
    ips = open('ips.txt', 'r') 
    for line in ips:
        filee = open(UPLOAD_FOLDER+'/'+file.filename, 'rb')
        requests.post(line, files = {'file':filee})
        filee.close()

    try:
        os.remove(UPLOAD_FOLDER+'/'+file.filename)
    except:
        print('Error ao deletar arquivo.')
    
    return 'ok'
    
if __name__ == '__main__':
    app.run(debug = True, host = socket.gethostbyname(hostname),  port = 5000)