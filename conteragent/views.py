from django.shortcuts import render, redirect
from .models import LPU
from .forms import LPUForm


def index(request):
    all_lpu = LPU.objects.all()
    return render(request, 'conteragent/index.html', context={
        'lpus': all_lpu
    })


def addlpu(request):
    data = dict()
    if request.method == 'GET':
        # блокировка доступа через ад строку
        if request.user.username == 'Deosz':
            data['form'] = LPUForm()
            return render(request, 'conteragent/addlpu.html', context=data)
        else:
            return render(request, 'layouts/page403.html')
    elif request.method == 'POST':
        # обработка данных формы добавления новости
        field_form = LPUForm(request.POST)
        field_form.save()
        return render(request, 'conteragent/index.html')


def editlpu(request, lpu_id):
    data = dict()
    editlpu = LPU.objects.get(id=lpu_id)
    if request.method == 'GET':
        data['lpu'] = editlpu
        data['form'] = LPUForm(instance=editlpu)
        return render(request, 'conteragent/editlpu.html', context=data)
    elif request.method == 'POST':
        filled_form = LPUForm(request.POST)
        if filled_form.is_valid():
            editlpu.name = filled_form.cleaned_data['name']
            editlpu.city = filled_form.cleaned_data['city']
            editlpu.address = filled_form.cleaned_data['address']
            editlpu.categoty = filled_form.cleaned_data['category']
            editlpu.save()
        return redirect('/conteragent/index')


def dellpu(request, lpu_id):
    data = dict()
    deleted_LPU = LPU.objects.get(id=lpu_id)
    if request.method == 'GET':
        data['lpu'] = deleted_LPU
        return render(request, 'conteragent/dellpu.html', context=data)
    elif request.method == 'POST':
        deleted_LPU.delete()
        return redirect('/conteragent/index')
