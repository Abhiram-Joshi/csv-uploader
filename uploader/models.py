from django.db import models
from account.models import User

# Create your models here.
class ContactsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=13)