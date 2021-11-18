from .models import ContactsModel
from celery import shared_task
import re
import csv
from website.celery import app
from django.contrib.auth import get_user_model

# @app.task
@shared_task
def csv_extract(username, file):
    User = get_user_model()
    csv_reader = csv.DictReader(file)

    phone_no_pattern = re.compile(r"(?P<ccode>\d{2})\s?(?P<number>\d{10})")

    for row in csv_reader:
        name = row["name"]
        phone_no = row["phone_no"]
        
        if match:=re.match(phone_no_pattern, phone_no):
            phone_no = int(match.group("ccode")+match.group("number"))
            print(ContactsModel.objects.create(name=name, phone_no=int(phone_no), user=User.objects.get(username=username)))