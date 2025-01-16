from .views import home,newUser,allUsers
from django.urls import path


urlpatterns=[
    path("home",home,name="home"),
    path("adduser",newUser,name="adduser"),
    path("allusers",allUsers,name="allusers")
]
