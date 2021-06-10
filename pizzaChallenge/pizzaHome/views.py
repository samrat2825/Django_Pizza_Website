from django.shortcuts import render
from .models import Pizza

# Create your views here.


def product(request):

    pizzas = Pizza.objects.first()
    print("---------------------------")
    print(pizzas)
    return render(request, 'product.html', {'pizzas': pizzas})


def index(request):

    pizzas = Pizza.objects.all()
    return render(request, 'index.html', {'pizzas': pizzas})
