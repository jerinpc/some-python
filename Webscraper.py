'''
from bs4 import BeautifulSoup
import requests

URL=''

def webscrape():
    response=requests.get(URL)
    soup=BeautifulSoup(response.text,'html.parser')
    content=soup.find('blockquote',class_='example').text
    print(content)

webscrap()
'''

from bs4 import BeautifulSoup 
import requests
from urllib.parse import urljoin
import urllib.request
import os

os.makedirs('Scraped_images',exist_ok=True)


URL='https://link.springer.com/article/10.1007/s10509-025-04496-7'

def scraper():
    response=requests.get(URL)
    if response.status_code==200:
        pass
    else:
        print('Failed to conntect',response.status_code)
    webdata=BeautifulSoup(response.text,'html.parser')
    return webdata

def webdatas():
    imagecontainer=[]
    soup=scraper()
    print('Title :',soup.title.text.strip())
    description=soup.find('meta', {'name':'dc.description'})
    print('\n')
    print('Description :',description.get('content').strip())
    print('\n')
    images=soup.find_all('img')
    for image in images:
        src=image.get('src')
        if src and 'MediaObjects' in src:
            full_url=urljoin(URL,src)
            imagecontainer.append(full_url)
    return imagecontainer
        
    
images=webdatas()

for index,url in enumerate(images,start=1):
    #print(f'{index} {image}')
    #extension = os.path.splitext(image)[1]
    resonse=requests.get(url)
    filename=f'Scraped_images/Figure{index}.png'
    with open(filename,'wb') as f:
        f.write(resonse.content)
    print(f'saved {filename}')
    
