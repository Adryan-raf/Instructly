from django.shortcuts import render, redirect, get_object_or_404
from appweb.models import Speaker
from appweb.forms import SpeakerForm
# Create your views here.
def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data["form"] = SpeakerForm()
    return render(request, 'form.html', data)

def speaker_list(request):
    lectures = Speaker.objects.all()
    return render(request, 'speaker_list.html', {'speaker': Speaker})


def speaker_create(request):
    if request.method == 'POST':
        form = speaker_create(request.POST)
        if form.is_valid():
            form.save()
            return redirect('speaker_list')
    else:
        form = speaker_create()
    return render(request, 'speaker_form.html', {'form': form})

def speaker_update(request, pk):
    lecture = get_object_or_404(Speaker, pk=pk)
    if request.method == 'POST':
        form = SpeakerForm(request.POST, instance=Speaker)
        if form.is_valid():
            form.save()
            return redirect('spekaer_list')
    else:
        form = SpeakerForm(instance=Speaker)
    return render(request, 'spekaer_form.html', {'form': form})


def speaker_delete(request, pk):
    Speaker = get_object_or_404(Speaker, pk=pk)
    if request.method == 'POST':
        Speaker.delete()
        return redirect('speaker_list')
    return render(request, 'speaker_confirm_delete.html', {'speaker': Speaker})

