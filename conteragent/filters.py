import django_filters
from django_filters import CharFilter
from django.forms import TextInput
from .models import LPU


class LpuFilter(django_filters.FilterSet):
    city = CharFilter(
        field_name="city",
        lookup_expr="startswith",
        widget=TextInput(attrs={"class": "form-control"}),
        label="Поиск по городу",
    )
    address = CharFilter(
        field_name="address",
        lookup_expr="startswith",
        widget=TextInput(attrs={"class": "form-control"}),
        label="Поиск по адресу",
    )
    name = CharFilter(
        field_name="name",
        lookup_expr="startswith",
        widget=TextInput(attrs={"class": "form-control"}),
        label="Поиск по бренду",
    )
