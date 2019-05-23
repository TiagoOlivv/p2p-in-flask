import os, json
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import time
import requests
UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['uploads'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    url = 'http://192.168.43.208:5002/'
    filename = secure_filename(str(file))
    file.save(os.path.join(app.config[UPLOAD_FOLDER], filename[12:-5]))	
    
    filee = open(UPLOAD_FOLDER+'/'+file.filename, 'rb')
    
    requests.post(url, files = {'file':filee})

    filee.close()

    try:
    	os.remove(UPLOAD_FOLDER+'/'+file.filename)
    except:
    	print('Error ao deletar arquivo.')
    
    return 'ok'
    
if __name__ == '__main__':
	app.run(debug=True, host = '192.168.43.179', port = '5000' )