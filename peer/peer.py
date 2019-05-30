from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import socket
import os, hashlib
import requests
import glob

app = Flask(__name__)
hostname = socket.gethostname()
BLOCKSIZE = 65536
hasher = hashlib.md5()

@app.route('/verifica', methods = ['GET', 'POST'])
def verifica():
	name_archive = request.data
	files = glob.glob('uploads/*')
	check = 0

	try:
		with open('uploads/' + name_archive.decode('utf8'), 'rb') as afile:
			buf = afile.read(BLOCKSIZE)
			while len(buf) > 0:
				hasher.update(buf)
				buf = afile.read(BLOCKSIZE)
				hash_code = hasher.hexdigest()
		print (hash_code) 
	except:
		print("deu erro")

	for line in files:
		if(line[8:] == name_archive.decode('utf8')):
			check = 1
			value = 'http://'+str(socket.gethostbyname(hostname))+':5002/'
			requests.post('http://192.168.0.4:5000/resposta',data = value)
			requests.post('http://192.168.0.4:5000/resposta',data = hash_code)
	
	if (check==0):
		requests.post('http://192.168.0.4:5000/resposta',data = 'false')
	
	requests.post('http://192.168.0.4:5000/recebeTorrent')
	
	return 'envia'

if __name__ == '__main__':
   app.run(debug = True, host = socket.gethostbyname(hostname),  port = 5002)