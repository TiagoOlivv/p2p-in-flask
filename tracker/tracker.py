from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import socket
import os
import requests

app = Flask(__name__)
hostname = socket.gethostname()

@app.route('/torrent', methods = ['GET', 'POST'])
def torrent():
	name_archive = request.data
	print("Tracker recebeu: ",name_archive)

	ips = ['http://192.168.0.4:5002/verifica','http://192.168.0.4:5003/verifica']
	
	for line in ips:
		requests.post(line,data = name_archive)

	return 'enviado'

@app.route('/recebeTorrent', methods = ['GET', 'POST'])
def recebeTorrent():
	file = open('file.torrent','rb').read()
	requests.post('http://192.168.0.4:5001/recebeTorrentPR',files = {'file':file})
	
	try:
		os.remove('file.torrent')
	except:
		print('Error ao deletar arquivo.')

	return 'ok'

@app.route('/resposta', methods = ['GET', 'POST'])
def resposta():
	resposta = request.data
	escreve(resposta)
	return 'enviado'

def escreve(nome):
	arq = open('file.torrent', 'a+')
	if(nome.decode('utf-8') != 'false'):
		arq.write(nome.decode('utf-8')) 
		arq.write('\n')
	arq.close()

if __name__ == '__main__':
   app.run(debug = True, host = socket.gethostbyname(hostname),  port = 5000)