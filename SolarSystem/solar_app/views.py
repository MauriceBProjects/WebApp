from django.shortcuts import render
from .models import Planet

def home(request):
    planets = Planet.objects.all()
    for planet in planets:
        planet.radius_class = get_radius_class(planet.radius)
        print(planet.radius)
    return render(request, 'home.html', {'planets':planets})


def get_radius_class(radius):
    if radius < 10:
        return 'small'
    elif 10 <= radius <= 20:
        return 'medium'
    else: 
        return 'large'
    
def learn(request):
    planets = Planet.objects.all()
    return render(request, 'learn.html', {'planets': planets})

def quiz(request):
    # Implement quiz logic here
    return render(request, 'quiz.html')

def help(request):
    return render(request, 'help.html')