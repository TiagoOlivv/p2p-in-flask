from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import socket
import random
import os
import string
import requests
import time

app = Flask(__name__)
hostname = socket.gethostname()
UPLOAD_PATH = "UPLOADS"

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
	if request.method == 'POST':
		f = request.files['file']
		files = {'file':f}
		upload_path = os.path.join(UPLOAD_PATH)
		f.save(os.path.join(upload_path, secure_filename(f.filename)))

		filee = open(UPLOAD_PATH+'/'+f.filename, "rb")
		
		requests.post('http://192.168.43.179:5000/', files = {'file':filee})
		
		return 'Arquivo enviado com sucesso, entre com o seu nome e extensão para poder baixa-lo.'
	else:
	   return render_template('upload.html')
	   code = request.form['file_code']

# @app.route('/download', methods = ['GET', 'POST'])
# def download():
#     if request.method == 'POST':
#         code = request.form['file_code']
#         folder = os.path.join(UPLOAD_PATH)

#         if not os.path.isdir (folder):
#             return "error: Nome indisponível"
#         files = os.listdir(folder)

#         if len(files) < 1:
#             return "error: Arquivo indisponível"

#         return send_from_directory(directory=folder, filename=code, as_attachment = True)
		
#     else:
#         return render_template('download.html')

@app.route('/', methods = ['GET'])
def index():
	return render_template('index.html')

if __name__ == '__main__':
   # app.run(debug = True, host = socket.gethostbyname(hostname),  port = 40000)
   app.run(debug = True, host = '192.168.43.21',  port = 5001)

