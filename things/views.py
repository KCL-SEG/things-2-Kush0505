from django.shortcuts import render
from things.forms import ThingForm

def home(request):
    form = ThingForm(request=POST or None)
    return render(request, 'home.html', {'form': form})
