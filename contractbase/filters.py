import django_filters
from django_filters import CharFilter
from django.forms import TextInput
from .models import Contract


class ContractFilter(django_filters.FilterSet):
    name = CharFilter(
        field_name="name",
        lookup_expr="startswith",
        widget=TextInput(attrs={"class": "form-control"}),
        label="Поиск по компании",
    )
