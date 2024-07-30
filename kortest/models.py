from django.db import models

# Create your models here.

class Item(models.Model):  # A Question Item
    qtext  = models.CharField(max_length=200)
    jimun = models.CharField(max_length=1000)
    # jimun_image = models.ImageField(upload_to='appname', null=True, blank=True) # image 

    ch1 = models.CharField(max_length=200) # choice 1
    ch2 = models.CharField(max_length=200)
    ch3 = models.CharField(max_length=200)
    ch4 = models.CharField(max_length=200)

    correct_answer = models.IntegerField()

    create_datetime = models.DateTimeField(auto_now=True, null=True)

class TestSheet(models.Model):
    items = models.ManyToManyField(Item)
    created_datetime = models.DateTimeField(auto_now=True, null=True, blank=True) # date & time of the test

class Answer(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    answer = models.IntegerField()
    create_datetime = models.DateTimeField()
