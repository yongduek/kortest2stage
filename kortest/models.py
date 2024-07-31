from django.db import models

# Create your models here.

class Item(models.Model):  # A Question Item
    name = models.CharField(max_length=200, default="Item")
    qtext  = models.CharField(max_length=200)
    jimun = models.CharField(max_length=1000)
    # jimun_image = models.ImageField(upload_to='appname', null=True, blank=True) # image 

    ch1 = models.CharField(max_length=200) # choice 1
    ch2 = models.CharField(max_length=200)
    ch3 = models.CharField(max_length=200)
    ch4 = models.CharField(max_length=200)

    correct_choice = models.CharField(max_length=100)

    created_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True) # 생성시간
    updated_datetime = models.DateTimeField(auto_now=True, blank=True, null=True) #

# m2m field does not allow ordering as itself.
# a way to solve it is using: through field: https://docs.djangoproject.com/en/5.0/topics/db/models/

class TestSheet(models.Model):
    name = models.CharField(max_length=100, default="TestSheet")
    items = models.ManyToManyField(Item, through="Membership")
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True) # 생성시간
    updated_datetime = models.DateTimeField(auto_now=True, blank=True, null=True) #

class Membership(models.Model): # association of Item to a TestSheet
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    testsheet = models.ForeignKey(TestSheet, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True) # 생성시간
    updated_datetime = models.DateTimeField(auto_now=True, blank=True, null=True) #

class Answer(models.Model):
    test_item = models.ForeignKey(Membership, on_delete=models.CASCADE)
    # item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    choice = models.CharField(max_length=100, default="0")
    iscorrect = models.BooleanField(default=False)
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True) # 생성시간
    updated_datetime = models.DateTimeField(auto_now=True, blank=True, null=True) #
