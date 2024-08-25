from django.shortcuts import render
from appweb.forms import SpeakerForm
# Create your views here.
def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data["form"] = SpeakerForm()
    return render(request, 'form.html', data)

