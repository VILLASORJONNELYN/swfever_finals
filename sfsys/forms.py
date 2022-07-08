from django.db.models import fields
from django.forms import ModelForm
from .models import DeathRecords


class deathForm(ModelForm):
    class Meta:
        model = DeathRecords
        fields = ['Region', 'Date', 'Num_Deaths']
