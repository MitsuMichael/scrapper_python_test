from flask import Flask, render_template, request
import os
import time
import glob

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods = ['POST', 'GET'])
def getradio():
	if request.method == 'POST':
		option = request.form['netRadio']
		print(option)
	return render_template('index.html', option=option)

@app.route('/run', methods = ['POST', 'GET'])
def run_():
	if request.method == 'POST':
	
		result = request.form
		option=result['rs']
		filename=result['fichier']#"facebook-scraper/data/out.csv"


		if option == 'fb':
			type_=result['type']
			id_=result['id']
			nb=result['nombre post']
			print(type_, id_, nb)
			if type_=='page':
				cmd="python facebook-scraper/facebook_scraper.py -a "+id_+" -f static/"+filename+" -p "+nb
				os.system(cmd)
				
			else:
				cmd="python facebook-scraper/facebook_scraper.py -g "+id_+" -f static/"+filename+" -p "+nb
				os.system(cmd)
				'''
				while True:
					os.system(cmd)
					time.sleep(600)
				'''
		elif option == 'tw':
			type_=result['type']
			nb=result['nombre post']
			id_=result['id']

			if type_=='hashtag':
				cmd="python twitter_scraper/main.py -t "+id_+" -f static/"+filename+" -p "+nb
				os.system(cmd)
			else:
				cmd="python twitter_scraper/main.py -t "+id_+" -f static/"+filename+" -p "+nb
				os.system(cmd)
		elif option == 'pt':
			email=result['email']
			pswd=result['pswd']
			mot_pt=result['mot_pt']

			cmd="python pinterest_scraper.py -m "+email+" -p "+pswd+" -k "+mot_pt+" -f static/"+filename
			os.system(cmd)
		else:
			pass

		return render_template("index.html",option=option)


@app.route('/results', methods = ['POST', 'GET'])
def result():
	
	return render_template('result.html')

@app.route('/download', methods = ['POST', 'GET'])
def download():
	#path=r"static"
	#file = glob.glob(path+"/*")
	
	file = glob.glob("static/*")
	print(file)
	
	latest_file = max(file, key=os.path.getctime)
	print(latest_file)
	latest_file1 = latest_file.split('/') #server online
	#latest_file1 = latest_file.split('\\') #server local
	print(latest_file1)
	filename = latest_file1[1]
	
	return render_template('download.html', file=filename, result=result)

@app.route('/progress', methods = ['POST', 'GET'])
def progress():

	return render_template('progress.html')


if __name__ == '__main__':
	# Threaded option to enable multiple instances for multiple user access support
    #app.run(threaded=True,port=5000)
    app.run(threaded=True,host='0.0.0.0')
