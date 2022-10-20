from queue import Empty
import bs4 as bs
import urllib.request

def search(search_term):
    definition = search_term
    url=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
    soup=bs.BeautifulSoup(url,'lxml')
    definitions=[]
    for paragraph in soup.find_all('p'):
        definitions.append(str(paragraph.text))
    if (definitions is Empty ):
        return False
    else :
        return definitions
