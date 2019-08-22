from django.core.management.base import BaseCommand, CommandError
from main.models import *
from .lib.googlelib import search
from .lib.utils import _get_search_url
import sys

def is_exist(link):
    try:
        Log.objects.get(link=link)
        return True
    except:
        return False

def put_in_log(link):
    l = Log()
    l.link = link
    l.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Grabing')
        MaterialPage.objects.all().delete()
        #for page in range(0,5):
        page = 0
        for word in Word.objects.all().order_by('-id'):
            #MaterialItem.objects.filter(word=word).delete()
            url = _get_search_url(word.name, page)
            print(word)
            if not is_exist(word):             
                start_position = 0
                search_results = search(word.name,page=page)
                if len(search_results['data'])> 50:
                    mp = MaterialPage()
                    mp.html = search_results['html']
                    mp.page = 1
                    mp.word = word
                    mp.search_url = search_results['url']
                    #import pdb; pdb.set_trace()
                    mp.save()
                    for result in search_results['data']:
                        start_position += 1
                        mi = MaterialItem()
                        mi.word = word
                        mi.title = result.name
                        mi.link = result.link
                        mi.material = mp
                        mi.page = page
                        mi.position = start_position
                        mi.save()
                        #print(result.name)
                        print(result.link)
                    put_in_log(word)
                else:
                    print('Captcha!!!!!!!!!!')
                    #sys.exit('Captcha!!!!!!!!!!')
            else:
                print('Exists!')
            #break