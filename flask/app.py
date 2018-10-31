from flask import Flask, render_template, request
from api import get_prob
app = Flask('Certified')

@app.route('/')

def home_page():
	return render_template('index.html')




@app.route('/id', methods = ['POST', 'GET'])

def certified():
	if request.method == 'GET':
		return render_template('certified.html')
	if request.method == 'POST':
		prob = get_prob(request.form['age'], request.form['subject'], \
			            request.form['gender'], request.form['education'])
		return render_template('certified.html', age = request.form['age'], \
								subject = request.form['subject'], \
								gender = request.form['gender'], \
								education = request.form['education'], \
								prob = prob)
	


if __name__ == '__main__':
	app.run()
