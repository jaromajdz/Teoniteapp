
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'teonitesp.settings'
django.setup()
from go.models import *
from django.db import connection

#cos=Links.objects.get(id_link=62)

#print(cos)
#Posts.objects.all().delete()
#Authors.objects.all().delete()

#post=Posts.objects.all()

#cos=Links.objects.get(id_link=62)

name='andrzejpiasecki'
d=Authors.objects.all()
id = [i.id_author for i in d if ''.join(i.author.lower().split()) == name ]
