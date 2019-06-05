from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import socket
import os, hashlib
import requests
import glob
import zipfile as zipf
import shutil

app = Flask(__name__)
hostname = socket.gethostname()
BLOCKSIZE = 65536
hasher = hashlib.md5()
kilobytes = 1024
megabytes = kilobytes * 1000
chunksize = int(1.4 * megabytes)   
UPLOAD_FOLDER = "uploads"
app.config['uploads'] = UPLOAD_FOLDER


@app.route('/Disponivel', methods = ['HEAD', 'GET', 'POST'])
def Disponivel():
	return 'ok'

@app.route('/verifica', methods = ['GET', 'POST'])
def verifica():
	name_archive = request.data
	files = glob.glob('uploads/*')
	check = 0
	brokers = 0
	url_tracker = ip_tracker()

	try:
		with open('uploads/' + name_archive.decode('utf8'), 'rb') as afile:
			buf = afile.read(BLOCKSIZE)
			while len(buf) > 0:
				hasher.update(buf)
				buf = afile.read(BLOCKSIZE)
				hash_code = hasher.hexdigest()
	except:
		print("deu erro")

	try:
		fromfile = 'uploads/'+str(name_archive.decode('utf8'))
		todir = 'result'

		absfrom, absto = list(map(os.path.abspath, [fromfile, todir]))
		parts = split(fromfile, todir, chunksize)

		brokers = glob.glob('result/*')
	except:
		print("deu erro")
	
	for line in files:
		if(line[8:] == name_archive.decode('utf8')):
			check = 1
			host = socket.gethostbyname(hostname)
			port = ':5002'
			value = 'http://' + host + port
			print(value)
			requests.post(url_tracker + '/resposta', data = value)
			requests.post(url_tracker + '/resposta', data = hash_code)
			requests.post(url_tracker + '/resposta', data = str(len(brokers)))
			
	if (check==0):
		requests.post(url_tracker + '/resposta', data = 'false')
		
	return 'envia'

@app.route('/upload2', methods = ['GET', 'POST'])
def upload2():
	file = request.files['file']
	upload_path = os.path.join(UPLOAD_FOLDER)
	file.save(os.path.join(upload_path, secure_filename(file.filename)))
	return 'ok'

@app.route('/arquivo', methods = ['GET', 'POST'])
def arquivo():
	file = request.data
	brokers = glob.glob('result/*')
	ini = 0
	fim = 0
	if(file.decode('utf-8') != 'todos'):
		for i,line in enumerate(file.decode('utf-8')):
			if(line=='-'):
				ini = str(file[:i].decode('utf-8'))
				fim = str(file[i+1:].decode('utf-8'))

		for i,line in enumerate(brokers):
			if(i+1 <= int(fim)):
				os.remove(line)

		for i,line in enumerate(brokers):
			if(i+1 > int(ini)):
				os.remove(line)

	zipar(['result','Tudo'])

	arquivo = open('nome.zip', 'rb').read()
	url_requerente = ip_requerente()
	requests.post(url_requerente + '/recebeZip', files = {'file':arquivo} )

	os.remove('nome.zip')
	shutil.rmtree('result', ignore_errors=True)

	return 'ok'

def zipar(arqs):
	with zipf.ZipFile('nome.zip','w', zipf.ZIP_DEFLATED) as z:
	    for arq in arqs:
	        if(os.path.isfile(arq)): 
	            z.write(arq)
	        else: 
	            for root, dirs, files in os.walk(arq):
	                for f in files:
	                    z.write(os.path.join(root, f))

def split(fromfile, todir, chunksize=chunksize):
	if not os.path.exists(todir):                 
		os.mkdir(todir)                           
	else:
		for fname in os.listdir(todir):            
			os.remove(os.path.join(todir, fname))
	partnum = 0
	try:
		input = open(fromfile, 'rb')                    
		while 1:                                      
			chunk = input.read(chunksize)              
			if not chunk:
				break
			partnum = partnum+1
			filename = os.path.join(todir, ('part%04d' % partnum))
			fileobj = open(filename, 'wb')
			fileobj.write(chunk)
			fileobj.close()                            
		input.close()
		assert partnum <= 9999                        
		
	except:
		print('arquivo não encontrado') 

	return partnum

def ip_tracker():
	with open('tracker.txt') as file:
		dump = file.read()
		dump = dump.splitlines()
		for ip in dump:
			url = str(ip)
			return url

def ip_requerente():
	with open('requerente.txt') as file:
		dump = file.read()
		dump = dump.splitlines()
		for ip in dump:
			url = str(ip)
			return url	

if __name__ == '__main__':
   app.run(debug = True, host = socket.gethostbyname(hostname),  port = 5002, threaded = True)