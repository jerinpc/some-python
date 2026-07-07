from bs4 import BeautifulSoup
import requests

URL=''

def webscrape():
    response=requests.get(URL)
    soup=BeautifulSoup(response.text,'html.parser')
    content=soup.find('blockquote',class_='abstract mathjax').text
    print(content)

webscrap()
