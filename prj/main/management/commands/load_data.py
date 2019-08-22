from django.core.management.base import BaseCommand, CommandError
from main.models import *
from prj.settings import BASE_DIR
class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Loading')
        
        Word.objects.all().delete()
        '''
        w = Word()
        w.name = 'разработка сайтов'
        w.save()

        w = Word()
        w.name = 'продвижение сайтов'
        w.save()
        '''

        with open(BASE_DIR+'/data/keys.csv', 'r') as f:
            for line in f.readlines():
                arr = line.split(',')
                print(arr[4])
                if(len(arr[4])>2):
                    w = Word()
                    w.name = arr[4]
                    w.save()                

        