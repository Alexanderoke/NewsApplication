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
  publish_date=[]

  for i in range(len(top_articles)):
    main_article=top_articles[i]

    news.apppend(main_article['title'])
    desc.append(main_article['description'])
    img.append(main_article['urlToImage'])
    publish_date.append(main_article['publishedAt'])
    url.append(main_article['"url'])

    contents= zip(news,desc,img,publish_date,url)



    return render_template('index.html',contents=contents)


  return render_template('index.html')

  if __name__=='__main__':
   app.run(debug=True)