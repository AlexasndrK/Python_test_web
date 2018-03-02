import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")

import django
django.setup()
#  Faker part of script

from faker import Faker
import random
from djangoApp.models import AccessRecords, Topic, Webpage

fakegen = Faker()
topic = ["News", "Social Networks", "Search", "Marketplace", "Games", "Photo"]


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topic))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        accRec = AccessRecords.objects.get_or_create(name=webpg, date=fake_date)


if __name__ == '__main__':
    print("starting feeding DB with fake data")
    populate(10)
    print("completed")
