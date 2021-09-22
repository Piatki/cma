from django import forms
from .models import ClientAppeal, MKB


class Appeal(forms.ModelForm):
    class Meta:
        model = ClientAppeal
        fields = ('lpu', 'date_create', 'author', 'info', 'task', 'diagnoz')


class MKB_block(forms.ModelForm):
    class Meta:
        model = MKB
        fields = ('name_mkb',)