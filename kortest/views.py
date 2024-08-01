from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Item, TestSheet, Membership, Answer

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, Welcome to KorTest by JSK Technology.")

def index(request):
    tslist = TestSheet.objects.all()

    context = {'tslist': tslist}
    return render(request, 'kortest/testsheet_list.html', context)
#

def testsheet(request, ts_name):
    # ts = TestSheet.objects.get(name=ts_name)
    ts = get_object_or_404(TestSheet, name=ts_name)
    context = {'ts': ts}
    return render(request, 'kortest/testsheet.html', context)

def answer_create(request, ts_name):
    ts = get_object_or_404(TestSheet, name=ts_name)
    context = {'ts': ts}
    return redirect('kortest:index')