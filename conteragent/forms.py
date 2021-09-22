from django import forms
from .models import LPU


class LPUForm(forms.ModelForm):
    class Meta:
        model = LPU
        fields = ('name', 'city', 'address', 'category')
