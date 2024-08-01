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
    print("------------------------")
    print(f"  kortest:answer_create({request}, {ts_name})")
    print("------------------------")
    
    ts = get_object_or_404(TestSheet, name=ts_name)
    
    print("  TS obtained: ", ts)
    for item in ts.items.all():
        ans_name = item.name + "_answer"
        answer = request.POST.get(ans_name)
        choices = [None, item.ch1, item.ch2, item.ch3, item.ch4]
        correct_choice = choices[int(item.correct_choice)]
        iscorrect = answer == correct_choice

        print("\t", item.name, item.correct_choice, f"correct='{correct_choice}'")
        print("\tAnswered:", answer)
        print("\tResult:", answer == correct_choice)
        # break
    context = {'ts': ts}
    return redirect('kortest:index')