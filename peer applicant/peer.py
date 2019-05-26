from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import socket
import os
import string
import requests

app = Flask(__name__)
hostname = socket.gethostname()
UPLOAD_PATH = "uploads"

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        files = {'file':f}
        upload_path = os.path.join(UPLOAD_PATH)
        f.save(os.path.join(upload_path, secure_filename(f.filename)))

        filee = open(upload_path+'/'+f.filename, "rb")
        
        requests.post('http://192.168.0.136:5000/', files = {'file':filee})

        filee.close()

        os.remove(upload_path+'/'+f.filename)     
        
        filee.close()
        return 'Arquivo enviado com sucesso, entre com o seu nome e extensão para poder baixa-lo.'
    else:
       return render_template('upload.html')

@app.route('/download', methods = ['GET', 'POST'])
def download():
    if request.method == 'POST':
        code = request.form['file_code']
        b = (str(code))
        requests.post('http://192.168.43.179:5000/download', data = b)
        
        # folder = os.path.join(UPLOAD_PATH)

        # if not os.path.lisdir(folder):
        #     return "error: Nome indisponível"
        # files = os.listdir(folder)

        # if len(files) < 1:
        #     return "error: Arquivo indisponível"

        #return send_from_directory(directory=folder, filename=code, as_attachment = True)
        return 'Download realizado com sucesso'

    else:
        return render_template('download.html')

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True, host = socket.gethostbyname(hostname),  port = 5001)