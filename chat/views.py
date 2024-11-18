from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    # cards = {'available_apps': Apps.objects.all(), "time_form": DateForm}
    return render(request, 'chat/index.html', {'room_name': 'main'})


def chat_room(request, room_name):
    return render(request, "chat/index.html", {"room_name": room_name})


def chat_page(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat/chat_page.html", context)