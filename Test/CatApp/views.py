from django.shortcuts import render

from .models import Human


# Create your views here.


def home(request):
    context = {}
    user = Human.objects.first()
    context['name'] = user.name
    context['age'] = user.age
    return render(request, "index.html", context)
