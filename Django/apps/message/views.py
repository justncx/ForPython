# -- coding: utf-8 --

from django.shortcuts import render
from models import UserMessage
import django
django.setup()
# Create your views here.

def getform(request):
    # all_messages = UserMessage.objects.all()
    all_messages = UserMessage.objects.filter(name = "lyc",address="XA")
    # for message in all_messages:
    #     print message.name
    if all_messages:
        message = all_messages[0]

    # if request.method == "POST":
    #     name = request.POST.get('name','')
    #     message = request.POST.get('message','')
    #     address = request.POST.get('address','')
    #     email = request.POST.get('email','')
    # user_message = UserMessage()
    # user_message.name = name
    # user_message.message = message
    # user_message.address = address
    # user_message.email = email
    # user_message.object_id = ' 2'
    # user_message.save()

    return render(request,'message_form.html',{
        "my_message":message
    })