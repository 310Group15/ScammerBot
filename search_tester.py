from bs4 import BeautifulSoup
#import requests, lxml


#finds wikipedia link about subject, returns false otherwise


def extract_search_term(subject):
 

  # headers = {
  #     'User-agent':
  #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
  # }

  # params = {
  #   "q": subject,
  #   "gl": "us",
  #   "hl": "en",
  #   "num": "100"
  # }

  # html = requests.get("https://www.google.com/search", headers=headers, params=params)
  # soup = BeautifulSoup(html.text, 'lxml')
  # print(soup.text)
  # for result in soup.select('.tF2Cxc')[:5]:
    
  #   title = result.select_one('.DKV0Md').text
  #   link = result.select_one('.yuRUbf a')['href']
  #   word = 'Wikipedia'
   
  #   if word in title:
      link = 'https://en.wikipedia.org/wiki/Abraham_Lincoln'
      return link
