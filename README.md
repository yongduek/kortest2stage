# kortest2stage

Target: Two stage testing

Currently, only one stage test of 20 items is under development, since it is also needed in reality.

---

Starting virtual environment. Creation of virtual environment is different depending on the operating system. Below is for Windows 10 environment.
```
cd kortes2stage
./venv/scripts/activate
```

Home directory is `kortest2stage`.
Start server
```
cd kortest2stage
python ./manage.py runserver
```
Open a web browser and type 
```
http://127.0.0.1:8000/kortest/
```

Open python shell & test data model
```
python manage.py shell
>>> import * from mydbtest
```
The file `mydbtest.py` contains several tests to examine functionings of data models I created.

### Todos
- [X] Make basic data models: Item, TestSheet, Membership, Answer
- [X] Do some tests of the model working: `mydbtest.py`
    - model creation
    - access to items and testsheets
    - access to Membership
- [] User manipulation and administration as a separate app (cf. Chapter 4 of [1], [2]).
- [] Include User model in Answer.
- [] Make a model connecting User and tests allocated with `done` flag. Only `done=False` tests will be displayed. Use the User model of Django as it is and make a model using `OneToOneField` (cf. Chapter 4 of [1], [2])


### References
1. Django by examples, 5th ed.
2. 점프 투 장고 (Jump to Django) in wikidocs (https://wikidocs.net/71259)
