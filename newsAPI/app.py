from flask import Flask , request, render_template
import requests
import json
import urllib

app = Flask(__name__)

@app.route('/headlines', methods=['POST', 'GET'])

def getheadlines():
	url = ('https://newsapi.org/v1/articles?source=associated-press&apiKey=f5d1e20dc1af4b5ea7222ba7f7b8c54c')
	response = requests.get(url)
	json_object = response.json()
	

	for i in range(len(json_object)):
		ParsedValue = json_object['articles'][i]['title']
		ParsedValue1 = json_object['articles'][i]['description']
		

	return render_template('head.html', headline_NEWS=ParsedValue, description=ParsedValue1)

@app.route('/')
def index():
	return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)