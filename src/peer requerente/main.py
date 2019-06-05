from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import socket
import os,hashlib
import requests
import concurrent.futures
from zipfile import ZipFile
import shutil
import time


app = Flask(__name__)
hostname = socket.gethostname()
UPLOAD_FOLDER = "uploads"
DOWNLOAD_FOLDER = "downloads"
app.config['uploads'] = UPLOAD_FOLDER
app.config['downloads'] = DOWNLOAD_FOLDER
tam = 1024
readsize = 1024
BLOCKSIZE = 65536
hasher = hashlib.md5()

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
	if request.method == 'POST':

		f = request.files['file']
		global nomeup
		nomeup = f.filename
		upload_path = os.path.join(UPLOAD_FOLDER)
		f.save(os.path.join(upload_path, secure_filename(f.filename)))
		url_tracker = ip_tracker()
		requests.post(url_tracker + '/upload')

		return 'Arquivo enviado com sucesso, entre com o seu nome e extensão para poder baixa-lo.'
	else:
	   return render_template('index.html')

@app.route('/Ativos', methods = ['GET', 'POST'])
def Ativos():
	file = request.files['file']
	upload_path = os.path.join(UPLOAD_FOLDER)
	file.save(os.path.join(upload_path,'file.torrent'))
	

	
	arquivo = open('uploads/file.torrent')
	
	for line in arquivo:
		filee = open('uploads/'+str(nomeup),'rb')
		teste = str(line[:-1])+'/upload2'
		requests.post(teste, files = {'file':filee})
			
	return 'ok'

@app.route('/download', methods = ['GET', 'POST'])
def download():
	global nomee
	if request.method == 'POST':
		if os.path.exists('uploads/file.torrent'):
			os.remove('uploads/file.torrent')
			code = request.form['file_code']
			name = (str(code))
			nomee = name
			url_tracker = ip_tracker()
			requests.post(url_tracker + '/torrent', data = name)
			return 'enviado'
		else: 
			code = request.form['file_code']
			name = (str(code))
			nomee = name
			url_tracker = ip_tracker()
			requests.post(url_tracker + '/torrent', data = name)
			return 'enviado'
	else:
		return render_template('index.html')	

@app.route('/recebeTorrentPR', methods = ['GET', 'POST'])
def recebeTorrentPR():
	file = request.files['file']
	file.save(os.path.join(app.config['uploads'], 'file.torrent'))
	res = []
	Dic = {}

	with open('uploads/file.torrent') as file:
		dump = file.read()
		dump = dump.splitlines()

	for ip in dump[::3]:
		url = str(ip)
		print('Requisitando em :', url)
		try:
			req = requests.get(url)
			res.append(req.elapsed.microseconds)
			Dic.update( { req.elapsed.microseconds:url} )
			print ('tempo de resposta:', res)
		except:
			print ('error')	

	Qnt_pacotes = dump[2]
	Qnt_pacotes = int(Qnt_pacotes)
	Qnt_peers = len(res)
	
	Peer_Prox = (min(sorted(Dic)))

	if(Qnt_peers ==2):
		for i,line in enumerate(sorted(Dic)):
			if(i == 1):
				Peer_Prox2 = Dic[line]

	if(Qnt_peers==1):
		requests.post(str(Dic[Peer_Prox])+'/arquivo',data = 'todos') 
	
	elif(Qnt_pacotes == 1 and Qnt_peers==2):
		requests.post(str(Dic[Peer_Prox])+'/arquivo',data = 'todos') 

	elif(Qnt_pacotes == 2 and Qnt_peers==2):
		requests.post(str(Dic[Peer_Prox])+'/arquivo',data = 'todos') 

	elif(Qnt_pacotes == 3 and Qnt_peers==2):
		requests.post(str(Dic[Peer_Prox])+'/arquivo',data = '3-1') 
		requests.post(str(Peer_Prox2)+'/arquivo',data = '1-0') 
		
	elif(Qnt_pacotes > 3 and Qnt_peers==2):
		qnt = (Qnt_pacotes//2)+1
		qnt2 = Qnt_pacotes - qnt
		requests.post(str(Dic[Peer_Prox])+'/arquivo',data = str(Qnt_pacotes)+'-'+str(qnt2)) 
		requests.post(str(Peer_Prox2)+'/arquivo',data = str(qnt2)+'-0')

	else:
		for line in sorted(Dic):
			teste = str(Qnt_pacotes)+'-'+str(Qnt_pacotes//2)
			requests.post(str(Dic[line])+'/arquivo',data = teste)
			Qnt_pacotes = Qnt_pacotes//2

	return 'ok'

@app.route('/recebeZip', methods = ['GET', 'POST'])
def recebeZip():
	file = request.files
	file['file'].save(os.path.join(app.config[DOWNLOAD_FOLDER],'nome.zip' )) 	
	zf = ZipFile('downloads/nome.zip', 'r')
	zf.extractall('result')
	zf.close()

	join('result/result',nomee)

	try:
		with open(nomee, 'rb') as afile:
			buf = afile.read(BLOCKSIZE)
			while len(buf) > 0:
				hasher.update(buf)
				buf = afile.read(BLOCKSIZE)
				hash_code = hasher.hexdigest()
	except:
		print("deu erro")

	hashcode2 = open('uploads/file.torrent','r')
	if(hash_code == hash_code):
		print('=========== Arquivo integro ===========')
	
	shutil.move(nomee, "downloads/"+nomee)
	os.remove('downloads/nome.zip')
	shutil.rmtree('result', ignore_errors=True)

	return 'ok'

def join(fromdir, tofile):
    output = open(tofile, 'wb')
    parts = os.listdir(fromdir)
    parts.sort()
    for filename in parts:
        filepath = os.path.join(fromdir, filename)
        fileobj = open(filepath, 'rb')
        while 1:
            filebytes = fileobj.read(readsize)
            if not filebytes:
                break
            output.write(filebytes)
        fileobj.close()
    output.close()

def ip_tracker():
	with open('tracker.txt') as file:
		dump = file.read()
		dump = dump.splitlines()
		for ip in dump:
			url = str(ip)
			return url

@app.route('/', methods = ['GET'])
def index():
	return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True, host = socket.gethostbyname(hostname),  port = 5001, threaded = True)