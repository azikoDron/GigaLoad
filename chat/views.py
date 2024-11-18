from django.shortcuts import render

# Create your views here.


def index(request):
    # cards = {'available_apps': Apps.objects.all(), "time_form": DateForm}
    return render(request, 'chat/index.html', {'room_name': 'main'})


def chat_room(request, room_name):
    return render(request, "chat/index.html", {"room_name": room_name})
