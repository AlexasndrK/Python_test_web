import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")

import django
django.setup()
#  Faker part of script

from faker import Faker
import random
from djangoApp.models import User
fakegen = Faker()


def populate(N=5):
    for entry in range(N):
        fake_firstName fake_secondName = fakegen.name()
        fake_email = fakegen.ascii_free_email()
        userPop, created = User.objects.get_or_create(firstName=fake_firstName, secondName=fake_secondName, email=fake_email)
        if not created:
            pritn("Error!")
            return False

if __name__ == '__main__':
    print("starting feeding DB with fake data")
    populate(10)
    print("completed")
