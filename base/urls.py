from django.urls import path
from . import views


urlpatterns = [
    path("", views.lobby, name="home"),
    path("room/", views.room, name="room"),
    path("get_token/", views.getToken), 
    path("create_member/", views.createMember),
    path("get_member/", views.getMember),
    path("register/", views.registerOrLogin, name="register_or_login"),
]
