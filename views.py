
from flask import Flask 
from flask import render_template, make_response, request
import urllib
import json


app = Flask(__name__)



@app.route('/')
def index():
	return render_template('index.html', name='Shubham')

@app.route('/authors')
def authors():
	response = urllib.request.urlopen('https://jsonplaceholder.typicode.com/users')
	users = json.loads(response.read().decode('utf-8'))

	response = urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts')
	posts = json.loads(response.read().decode('utf-8'))

	for a_user in users:
		no_of_posts = 0
		for a_post in posts:
			if a_user['id'] == a_post['userId']:
				no_of_posts += 1

		a_user['no_of_posts'] = no_of_posts

	return render_template('authors.html', authors = users)			


@app.route('/setcookie')
def set_cookie():
	response_s = make_response('<h1>You are done with setting cookies. </h1><p> Visit the /getcookies page to have a look at them.</p>')
	if 'name' not in request.cookies:
		response_s.set_cookie('name', 'Shubham')
	if 'age' not in request.cookies:
		response_s.set_cookie('age', '20')

	return response_s	
		
@app.route('/getcookies')
def get_cookie():
	return render_template('fetch_cookie.html', name = request.cookies.get('name'), age = request.cookies.get('age'))

@app.route('/robots.txt')
def deny_request():
	return render_template('deny.html'), 403

@app.route('/html')
def render_html() :
	return render_template('lorem_ipsum.html', title="Title passed from view to template", text="Shubham Kumar renders it.")

@app.route('/input', methods = ['GET', 'POST'])
def post_request():
	if request.method == 'POST':
		text_inp = request.form['text_inp']
		print('Input : '+ text_inp)
		return render_template('post.html', text_inp=text_inp)
	return render_template('post.html')	


if __name__ == '__main__':
	app.run(debug = True)
