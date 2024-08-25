from django.forms import ModelForm
from appweb.models import Speaker


class SpeakerForm(ModelForm):
    class Meta:
        model = Speaker
        fields = ["name", "email", "theme", "synopsis"]
