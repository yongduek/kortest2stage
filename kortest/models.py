from django.db import models

# Create your models here.

class Item(models.Model):  # A Question Item
    qtext  = models.CharField(max_length=200)
    qjimun = models.CharField(max_length=1000)
    # qjimun_image = models.ImageField(upload_to='appname', null=True) # image 

    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200)
    choice4 = models.CharField(max_length=200)

    correct_answer = models.IntegerField()

    create_datetime = models.DateTimeField(auto_now=True, null=True)

class TestSheet(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

class ListofTestSheets(models.Model):
    testsheet = models.ForeignKey(TestSheet, on_delete=models.CASCADE)
    datetime = models.DateTimeField() # date & time of the test

class Answer(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    answer = models.IntegerField()
    create_datetime = models.DateTimeField()


class AnswerSheet(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

class ListofAnswerSheet(models.Model):
    answersheet = models.ForeignKey(AnswerSheet, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)