from flask import Flask, render_template
from app import templates
from newsapi import NewsApiClient
import config
app = Flask(__name__)

@app.route("/")
def index():
  newsapi = NewsApiClient(api_key="eee9e812d2274500b4bb312f3a572be0")
  top_headlines= newsapi.get_top_headlines(sources= 'bbc-news')
  all_articles= newsapi.get_everything(sources='bbc-news')
  
  

  top_articles= top_headlines['articles']
  a_articles= all_articles['articles']

  news=[]
  img=[]
  url=[]
  desc=[]
  publish_date=[]

  

  for i in range(len(top_articles)):
    main_article=top_articles[i]

    news.append(main_article['title'])
    desc.append(main_article['description'])
    img.append(main_article['urlToImage'])
    publish_date.append(main_article['publishedAt'])
    url.append(main_article['url'])


  news_all=[]
  img_all=[]
  url_all=[]
  desc_all=[]
  publish_date_all=[]

  for l in range(len(a_articles)):
    a_article=a_articles[l]

    news_all.append(a_article['title'])
    desc_all.append(a_article['description'])
    img_all.append(a_article['urlToImage'])
    publish_date_all.append(a_article['publishedAt'])
    url_all.append(a_article['url'])

  contents= zip(news,desc,img,publish_date,url)
  all= zip(news_all,desc_all,img_all,publish_date_all,url_all)



  return render_template('index.html',contents=contents,all=all)


  # return render_template('index.html')

  if __name__=='__main__':
   app.run(debug=True)