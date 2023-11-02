from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name="home"),
    path('uploaddata',views.uploaddata, name="uploaddata"),
    path('querybuilder',views.querybuilder, name="querybuilder"),
    path('users',views.users, name="users"),
    path('login',views.manageLogin, name="login"),
    path('logout',views.manageLogout, name="logout"),
    path('addup',views.addup, name="addup")

]