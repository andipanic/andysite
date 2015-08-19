from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "title": "IRC",
        "heading": "IRC Related App!",
        "body": "Considering putting a IRC web client here.  We shall look into it and see.  Either way, something IRC related.",
        "nav": "irc",
    }
    return render(request, 'irc.html', context)
