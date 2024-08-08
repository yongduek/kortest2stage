# account/urls.py
# ref: https://wikidocs.net/71259 점프 투 장고

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 

app_name = 'account'


urlpatterns = [
    path('login/', 
         auth_views.LoginView.as_view(template_name='account/login.html'), 
         name='login'),
    path('logout/', views.logout_view, name='logout')
]