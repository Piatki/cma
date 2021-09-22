from django.shortcuts import render, redirect
from .models import Client, ClientAppeal, MKB
from .forms import ClientForm, Appeal, MKB_block


def index(request):
    all_clients = Client.objects.all()
    return render(request, 'clients/index.html', context={
        'clients': all_clients
    })


def clientcase(request, client_id):
    client = Client.objects.get(id=client_id)
    return render(request, 'clients/clientcase.html', context={
        'client': client
    })


def addclient(request):
    data = dict()
    if request.method == 'GET':
        if request.user.username == 'Deosz':
            data['form'] = ClientForm()
            return render(request, 'clients/addclient.html', context=data)
        else:
            return render(request, 'layouts/page403.html')
    elif request.method == 'POST':
        field_form = ClientForm(request.POST)
        field_form.save()
        return redirect('/clients/index')


def delclient(request, client_id):
    data = dict()
    deleted_Client = Client.objects.get(id=client_id)
    if request.method == 'GET':
        data['client'] = deleted_Client
        return render(request, 'clients/delclient.html', context=data)
    elif request.method == 'POST':
        deleted_Client.delete()
        return redirect('/clients/index')


def editclient(request, client_id):
    data = dict()
    editclient = Client.objects.get(id=client_id)
    if request.method == 'GET':
        data['client'] = editclient
        data['form'] = ClientForm(instance=editclient)
        return render(request, 'clients/editclient.html', context=data)
    elif request.method == 'POST':
        filled_form = ClientForm(request.POST)
        if filled_form.is_valid():
            editclient.name = filled_form.cleaned_data['name']
            editclient.date_birthday = filled_form.cleaned_data['date_birthday']
            editclient.company = filled_form.cleaned_data['company']
            editclient.program = filled_form.cleaned_data['program']
            editclient.police_num = filled_form.cleaned_data['police_num']
            editclient.date_start_police = filled_form.cleaned_data['date_start_police']
            editclient.date_finish_police = filled_form.cleaned_data['date_finish_police']
            editclient.mail = filled_form.cleaned_data['mail']
            editclient.phone_number = filled_form.cleaned_data['phone_number']
            editclient.save()
        return redirect('/clients/index')


def clientappeal(request, client_id):
    client = Client.objects.get(id=client_id)
    all_mkbs = MKB.objects.all()
    return render(request, 'clients/clientappeal.html', context={
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