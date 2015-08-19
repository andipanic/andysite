from django.shortcuts import render

def home(request):
    context = {
            "title": "Home",
            "heading": "This is a heading",
            "body": "This is the body",
    }
    return render(request, 'home.html', context)
