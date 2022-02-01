from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route("/")
def index():
  newsapi = NewsApiClient(api_key="eee9e812d2274500b4bb312f3a572be0")
  top_headlines= newsapi.get_top_headlines(sources='the-verge')

  top_articles= top_headlines['articles']

  news=[]
  img=[]
  url=[]
  desc=[]

  for i in range(len(top_articles)):
    main_article=top_articles[i]

    news.apppend(main_article['title'])
    

    return render_template('index.html')


  return render_template('index.html')

  if __name__=='__main__':
   app.run(debug=True)