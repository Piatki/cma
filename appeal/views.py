from django.shortcuts import render, redirect
from .models import ClientAppeal, MKB
from clients.models import Client
from .forms import Appeal


def clientappeal(request, client_id):
    client = Client.objects.get(id=client_id)
    all_mkbs = MKB.objects.all()
    return render(request, 'appeal/clientappeal.html', context={
        'mkbs': all_mkbs,
        'client': client
    })


def formappeal(request, appeal_id):
    data = dict()
    if request.method == 'GET':
        if request.user.username == 'Deosz':
            data['form'] = Appeal()
            return render(request, 'clients/formappeal.html', context=data)
        else:
            return render(request, 'layouts/page403.html')
    elif request.method == 'POST':
        appeal = ClientAppeal.objects.get(id=appeal_id)
        # обработка данных формы добавления новости
        field_form = Appeal(request.POST)
        field_form.save()
        return redirect('/clientappeal', context={
            'appeal': appeal
        })
