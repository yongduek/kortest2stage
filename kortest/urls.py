from django.urls import path

from . import views 

app_name = 'kortest'

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:ts_name>/', views.testsheet, name='testsheet'),
    path('answer_create/<str:ts_name>/', views.answer_create, name='answer_create')
]