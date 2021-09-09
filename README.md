# Flask Learning

~This repository contains some basic API endpoints written using Flask.

How to use:

->Clone the repository

-> Create a virtual environment and activate it. We will be setting Python 3 as default in the virtual environment. Although this step is not mandatory but it is recommended so that the development environment is isolated.

-> virtualenv venv --python=`which python3`

-> source venv/bin/activate

-> Install dependencies

-> pip install -r requirements.txt

-> Run the application within the devserver provided by flask

-> cd hpdf-tasks/

-> python views.py

-> All set. Fire up any web browser and go to http://127.0.0.1:5000/ to see the application live!
Tasks
These tasks consists of implementation of multiple endpoints which serve different needs. The following tasks are are accomplished.

 1.) Add an endpoint at / that displays Hello World along with your first name (and slack username)
 
 2.) Add and endpoint at /authors which fetches a list of authors and count of their posts using the given JSON data available via URLs https://jsonplaceholder.typicode.com/users and https://jsonplaceholder.typicode.com/posts

 3.) Add an endpoint at /setcookie which sets a cookie with values name=<your-first-name> and age=<your-age if not set already.
 
 4.) Add an endpoint at /getcookies which displays the values of the cookie that has been set with /setcookie endpoint.
 
 5.) Deny request to /robots.txt endpoint with 403 (Forbidden) status code.
 
 6.) Add an endpoint at /html displaying some placeholder HTML text. Lorem Ipsum by INITIALIZR was used here.
 
 7.) Display a form containing a textbox at /input endpoint.
 Upon submitting the form at /input, send the data via a POST request to /input endpoint. This /input endpoint should display the text data received via the request instead of the form. Also log the received data to STDOUT.


**Requirements**

~ Python 3.x
~ Flask
