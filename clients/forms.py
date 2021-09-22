from django import forms
from .models import Client, ClientCase, ClientAppeal, MKB


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'date_birthday', 'company', 'program', 'police_num', 'date_start_police', 'date_finish_police', 'mail', 'phone_number')


class Case(forms.ModelForm):
    class Meta:
        model = ClientCase
        fields = ('num_case', 'date_start_appeal', 'date_finish_appeal', 'status', 'mkb_block', 'diagnoz', 'coordinator')


class Appeal(forms.ModelForm):
    class Meta:
        model = ClientAppeal
        fields = ('lpu', 'date_create', 'author', 'info', 'task', 'diagnoz')


class MKB_block(forms.ModelForm):
    class Meta:
        model = MKB
        fields = ('name_mkb',)