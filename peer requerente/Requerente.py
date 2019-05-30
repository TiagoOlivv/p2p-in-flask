from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import socket
import os
import requests

app = Flask(__name__)
hostname = socket.gethostname()
UPLOAD_FOLDER = "uploads"
app.config['uploads'] = UPLOAD_FOLDER

@app.route('/download', methods = ['GET', 'POST'])
def download():
	if request.method == 'POST':
		code = request.form['file_code']
		name = (str(code))
		requests.post('http://192.168.0.4:5000/torrent', data = name)
		return 'enviado'
	else:
		return render_template('download.html')	

@app.route('/recebeTorrentPR', methods = ['GET', 'POST'])
def recebeTorrentPR():
	# file = request.files['file']
	# file.save(os.path.join(app.config['uploads'], 'file.torrent'))
	
	# file2 = open('uploads/file.torrent','rb').read()
	# print(file2.decode('utf-8'))

	with open('uploads/file.torrent') as file:
		dump = file.read()
		dump = dump.splitlines()
		for ip in dump[::2]:
			url = str(ip)
			print('Requisitando em :', url)
			req = requests.get(url)
			time = req.elapsed
			print ('tempo de resposta:', time)

		
			# try:
			# 	url = str(ip)
			# 	r = requests.head(ip)

			# 	if r.status_code == 200 :
			# 		print("Servidor Disponivel")
			# 		contServer = contServer + 1
			# 		cpu = requests.get(ip)
			# 		alive = ip                      
			# 		print(cpu.json())
			# 		cpuUse.append(cpu.json()['CPU'])

			# except:
			# 	print("Servidor Indisponivel")
			
	# time = requests.head('http://192.168.11.8:5000/')

	return 'ok'

@app.route('/', methods = ['GET'])
def index():
	return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True, host = socket.gethostbyname(hostname),  port = 5001)