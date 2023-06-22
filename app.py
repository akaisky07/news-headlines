from flask import Flask, render_template, request
import requests

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
API_KEY= '80c48518a0144aefb9d836cb75285f13'
@app.route('/get_news', methods=['POST'])
def get_news():
    # get the user's request
    topic = request.form['topic']
    # make a request to the NewsAPI
    url = f'https://newsapi.org/v2/top-headlines?q={topic}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    # return the data to the user
    return render_template('news.html', articles=articles)

if __name__=='__main__':
	app.run(debug=True)
