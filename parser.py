import requests
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

def get_scores(news):
  sia = SIA()
  pol_score = sia.polarity_scores(news)
  return pol_score


def parse_content(js):
  for i in js['results']:
    news_id = i['id']
    domain = i['source']['domain']
    title = i['title']
    scores = get_scores(title)
    published_at = i['published_at']
    url = i['url']
    currencies = []
    if 'currencies' in i:
      for c in i['currencies']:
        currencies.append(c['code'])

    print(title)
    print(scores)
    print("\n")


def get_news(url):
  while True:
    res = requests.get(url)
    #print(res.status_code, res.reason)
    data = json.loads(res.text)
    if data['next'] == None:
      break
    else:
      parse_content(data)
      url = data['next']



# url = "https://cryptopanic.com/api/posts/?auth_token=2361711c64aa03bb8fac7c8f25f8b0f4d65b70d2&currencies=ETH"
url = "https://cryptopanic.com/api/posts/?auth_token=2361711c64aa03bb8fac7c8f25f8b0f4d65b70d2"
get_news(url)