from django.contrib import admin
from django.urls import re_path
from .import views



urlpatterns = [
    re_path(r'^submit/login/user/$',views.submit_login_user,name='submit_login_user')    # regex hamanshore submit/login/user (haman addresi ke dar postman mizani baray ersal dadeh ) ke eshareh mikoneh be ghsmat urls def submit_expense

]