from django.db import models

class Tweets(models.Model):
    # depois de inserir um novo modelo, é necessário digitar no terminal:
    # python manage.py makemigrations, feito isso, será criada uma nova migration
    # feito isso, deve-se digitar no terminal: python manage.py migrate
    user = models.CharField('User', max_length=20, default="lala")
    date = models.DateField('Data')
    text = models.CharField('Tweet', max_length=280)
    link = models.CharField('Link', max_length=280, default=" ")
