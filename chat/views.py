from django.shortcuts import render

# Create your views here.


def index(request):
    #cards = {'available_apps': Apps.objects.all(), "time_form": DateForm}
    return render(request, 'chat/index.html')