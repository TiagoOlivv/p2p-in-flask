from flask import Flask, render_template, request, send_from_directory
from werkzeug import secure_filename
import random
import os
import string

app = Flask(__name__)
UPLOAD_PATH = "UPLOADS"

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        upload_path = os.path.join(UPLOAD_PATH)
        f.save(os.path.join(upload_path, secure_filename(f.filename)))
        return 'Arquivo enviado com sucesso, entre com o seu nome e extensão para poder baixa-lo.'
    else:
       return render_template('upload.html')
       code = request.form['file_code']

@app.route('/download', methods = ['GET', 'POST'])
def download():
    if request.method == 'POST':
        code = request.form['file_code']
        folder = os.path.join(UPLOAD_PATH)

        if not os.path.isdir (folder):
            return "error: Nome indisponível"
        files = os.listdir(folder)

        if len(files) < 1:
            return "error: Arquivo indisponível"

        return send_from_directory(directory=folder, filename=code, as_attachment = True)
        
    else:
        return render_template('download.html')

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
   app.run(host='127.0.0.1')