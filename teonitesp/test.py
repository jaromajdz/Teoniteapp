import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'teonitesp.settings'
django.setup()
from go.models import *


cos = Posts.objects.get(id_post=1)
print(cos.post)
