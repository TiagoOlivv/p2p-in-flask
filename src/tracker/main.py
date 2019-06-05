from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import socket
import os
import requests
import time

app = Flask(__name__)
hostname = socket.gethostname()

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
	with open('peer.txt') as file:
		dump = file.read()
		dump = dump.splitlines()
		for ip in dump:
			try:
				res = requests.head(str(ip)+'/Disponivel')
				if res.status_code == 200:
					escreve2(str(ip))
			except:
				print("Servidor Indisponivel")

	time.sleep(2)
	url = ip_requerente()
	arq = open('file2.torrent', 'rb').read()
	requests.post(str(url)+'/Ativos',files = {'file':arq} )
	os.remove('file2.torrent')
	return 'ok'

@app.route('/torrent', methods = ['GET', 'POST'])
def torrent():
	if os.path.exists('file.torrent'):
		os.remove('file.torrent')

	arq = open('file.torrent', 'w+')
	arq.close()

	name_archive = request.data
	with open('peer.txt') as file:
		dump = file.read()
		dump = dump.splitlines()
		for ip in dump:
			try:
				requests.post(ip + '/verifica', data = name_archive)
			except:
				print("Servidor Indisponivel")

	time.sleep(2)
	file = open('file.torrent','rb').read()
	url = ip_requerente()
	requests.post(url + '/recebeTorrentPR',files = {'file':file})
	return 'enviado'

@app.route('/recebeTorrent', methods = ['GET', 'POST'])
def recebeTorrent():
	file = open('file.torrent','rb').read()
	url = ip_requerente()
	requests.post(url + '/recebeTorrentPR',files = {'file':file})
	os.remove('file.torrent')
	return 'ok'

@app.route('/resposta', methods = ['GET', 'POST'])
def resposta():
	resposta = request.data
	escreve(resposta)
	return 'enviado'

def escreve(nome):
	arq = open('file.torrent', 'a+')
	if((nome.decode('utf-8') != 'false')):
		arq.write(nome.decode('utf-8')+'\n') 
	arq.close()

def escreve2(nome):
	arq = open('file2.torrent', 'a+')
	arq.write(nome+'\n') 
	arq.close()

def ip_requerente():
	with open('requerente.txt') as file:
		dump = file.read()
		dump = dump.splitlines()
		for ip in dump:
			url = str(ip)
			return url

if __name__ == '__main__':
   app.run(debug = True, host = socket.gethostbyname(hostname),  port = 5000, threaded = True)