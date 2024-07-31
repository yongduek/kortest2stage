import random 
from kortest.models import Item, TestSheet, Membership, Answer

# 0. this is simulation.
#    Every table is cleaned before starting.
Item.objects.all().delete()
Membership.objects.all().delete()
TestSheet.objects.all().delete()
Answer.objects.all().delete()

# 1. create 20 items
def get_item_name(i):
    return f"Item_1{i:04}"

nitems = 20
for ii in range(nitems):
    i = ii + 1
    name = get_item_name(i) 
    item = Item(name = name,
                qtext = f"Question text of {name}",
                jimun = f"이것은 지문입니다 {name}",
                ch1 = f"첫번째 초이스 {name}",
                ch2 = f"두번째 초이스 {name}",
                ch3 = f"세번째 초이스 {name}",
                ch4 = f"네번째 초이스 {name}",
                correct_choice = 1 + i%4)
    
    item.save()

# 2 create two test sheets,
#   testsheet1 from odd numbers of items
#   testsheet2 from even numbers of items
#   ref: https://docs.djangoproject.com/en/5.0/topics/db/models/

test1 = TestSheet.objects.create(name = "TestSheet_1_odd")
test2 = TestSheet.objects.create(name = "TestSheet_2_even")
list_tests = [test1, test2]
# this is done by creating Memberships
for i in range(1, nitems+1):
    name = get_item_name(i)
    print(f"allocating item {name}")
    if i%2 == 0:  # even 
        member = Membership(item=Item.objects.get(name=name),
                            testsheet=list_tests[1])
    else:
        member = Membership(item=Item.objects.get(name=name),
                            testsheet=list_tests[0])
    member.save()
#

# 3. Now check the status of the testsheets
def print_ts(t11):
    print("TS Name: ", t11.name)
    for it in t11.items.all():
        print(it.name)
        print(it.qtext)
        print(it.jimun)
        print('\t', it.ch1)
        print('\t', it.ch2)
        print('\t', it.ch3)
        print('\t', it.ch4)
        print("correct answer = ", it.correct_choice)
        print(it.created_datetime)
        print(it.updated_datetime)
        print()
    #

print("----")
print("  TestSheet for Odd numbered items")
t1 = TestSheet.objects.get(name="TestSheet_1_odd")
print_ts(t1)

print("----")
print("  TestSheet for even numbered items")
t2 = TestSheet.objects.get(name="TestSheet_2_even")
print_ts(t2)


# 4. Now let's make answers to items in testshee1
for item in t1.items.all():
    choice = str(random.randint(1,4))
    ans = Answer(test_item = Membership.objects.get(item=item, testsheet=t1),
                 choice = choice,
                 iscorrect = int(choice) == int(item.correct_choice))
    ans.save()
#

def print_answers():
    for a in Answer.objects.all():
        print(a.test_item.testsheet.name)
        print(a.test_item.item.name)
        print("user choice: ", a.choice)
        print("correct choice: ",  a.test_item.item.correct_choice)
        print("result: ", a.iscorrect)
        print(a.created_datetime)
        print(a.updated_datetime)
        print()
#

print_answers()
