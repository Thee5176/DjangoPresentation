from django.shortcuts import render
from django.http import HttpResponse


# def homepage_view(request):
#     message = "Welcome, this is the homepage of my website."
#     return message

# def homepage_view(request):
#     title = "Homepage"
#     message = "Welcome, this is the homepage of my website."
#     return HttpResponse(message)


def homepage_view(request):
    title = "Homepage"
    message = "Welcome, this is the homepage of my website."

    context = {
        "title": title,
        "message": message,
    }

    return render(request, "home.html", context)
