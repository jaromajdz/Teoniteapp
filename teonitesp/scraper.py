
import os
import django
from bs4 import BeautifulSoup
import requests
import binascii
from time import gmtime, strftime

os.environ['DJANGO_SETTINGS_MODULE'] = 'teonitesp.settings'
django.setup()
from go.models import *



#scraper

url='http://teonite.com/blog/'

    #save to a few line of code could then be repeated
class Beauty(BeautifulSoup):

    def __init__(self, url):
        BeautifulSoup.__init__(self, self.get_page(url), 'html.parser')

    def get_page(self, url):
        result = requests.get(url)
        return result.content

def post_exists(value):
    try:
        cos = Posts.objects.get(link=value)
        return cos
    except:
        return False

def dodaj_author(value):
    if Authors.objects.filter(author=value).exists():
        return Authors.objects.get(author=value)
    else:
        cos = Authors(author=value)
        cos.save()
        return cos

def update_item(item):
    it=Posts.objects.get(link=item['link'])
    crc=str(binascii.crc32(item['post'].encode('utf-8')))
    if not crc==it.crc:
        it.post=item['post']
        it.crc=crc
        it.update()

def save_item(item):
    id_author = dodaj_author(item['author'])

    cos = Posts(
        post=item['post'],
        id_author =id_author,
        link = item['link'],
        crc=str(binascii.crc32(item['post'].encode('utf-8')))
        )
    cos.save()

def first_url(url):
    soup = Beauty(url)
    return soup.body.div.main.article.header.h2.a['href']
def scraper_loop(url):
    item ={}
    item['link'] = first_url(url)

    while item['link']:
        soup = Beauty(url + item['link'][6:])

        item['author'] = soup.find(class_='author-content').h4.text
        item['post'] = soup.body.div.main.article.find_all(class_='post-content')
    #content from article. It takes text from all tags having text attribute.
        item['post']=''.join(i.text for i in item['post'] if hasattr(i,'text'))

    #Save item or breake job when the link exists
        if not post_exists(item['link']):
            save_item(item)
    #if a link is not in database will be add added or if it exiets stop the loop
        else:
            update_item(item)

    #check for next post(link) if is no more then finish the loop
        if soup.body.div.main.ul.li.a:
            item['link'] = soup.body.div.main.ul.li.a['href']
        else:
            item['link']=''
    #    yield item
    #Get link  to next post if exists, finish the job when is no more posts


print('Getting data from teonite.com/blog')
scraper_loop(url)

with open('log.txt', 'a') as f:
	f.write(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
	f.closed

