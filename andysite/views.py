from django.shortcuts import render

def home(request):
    context = {
            "title": "Home",
            "heading": "Welcome to my website!",
            "body": "As you can see here, I have not much to show at the moment.  Soon enough real stuff will be here!",
            "nav": "home",
    }
    return render(request, 'home.html', context)
