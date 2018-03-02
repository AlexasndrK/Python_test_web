from django.shortcuts import render
from django.http import HttpResponse
from djangoApp.models import Topic, Webpage, AccessRecords, User
# Create your views here.


def index(request):
    import random
    import string
    newValuev = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(10))
    html = "<em><h1>{}</h1></em>".format(newValuev)
    my_dict = {"insert_me": html}
    return render(request, 'index.html', context=my_dict)


def help(request):
    solution = {'solution': "Relax and enjoy your time"}
    return render(request, 'help.html', context=solution)


def testHtml(request):
    test_dict = {"data": "Animus quod perdidit optat, Atque in praeterita se totus imagine versat"}
    web_inst = AccessRecords.objects.order_by('date')
    web_dict = {"access": web_inst}
    return render(request, 'test.html', context=web_dict)


def users(request):
    user_inst = User.objects.order_by('firstName')
    user_dict = {"userdata": user_inst}
    return render(request, 'users.html', context=user_dict)
