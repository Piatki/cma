from django import forms
from .models import Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ('name', 'num1', 'service1', 'description1', 'categories1', 'num2', 'service2', 'description2', 'categories2', 'num3', 'service3', 'description3', 'categories3', 'num4', 'service4', 'description4', 'categories4', 'num5', 'service5', 'description5', 'categories5', 'num6', 'service6', 'description6', 'categories6', 'num7', 'service7', 'description7', 'categories7', 'num8', 'service8', 'description8', 'categories8', 'num9', 'service9', 'description9', 'categories9', 'num10', 'service10', 'description10', 'categories10',)