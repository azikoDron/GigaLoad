from django.urls import path

from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('', views.chat_page, name='index'),
    path("<str:room_name>/", views.chat_room, name="chat_room"),

    path("", views.chat_page, name="chat_page"),
    # authentication section
    path("auth/login/", LoginView.as_view(template_name="chat/login_page.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
    ]