from django.shortcuts import render, redirect
from .models import Contract
from .forms import ContractForm


def index(request):
    all_contracts = Contract.objects.all()
    return render(request, 'contractbase/index.html', context={
        'contracts': all_contracts
    })


def contractread(request):
    return render(request, 'contractbase/contractread.html')


def editcontract(request, contract_id):
    data = dict()
    editcontract = Contract.objects.get(id=contract_id)
    if request.method == 'GET':
        data['contract'] = editcontract
        data['form'] = ContractForm(instance=editcontract)
        return render(request, 'contractbase/editcontract.html', context=data)
    elif request.method == 'POST':
        filled_form = ContractForm(request.POST)
        if filled_form.is_valid():
            editcontract.name = filled_form.cleaned_data['name']
            editcontract.num = filled_form.cleaned_data['num']
            editcontract.service = filled_form.cleaned_data['service']
            editcontract.description = filled_form.cleaned_data['description']
            editcontract.category = filled_form.cleaned_data['category']
            editcontract.save()
        return redirect('/contractbase/index')


def delcontract(request, contract_id):
    data = dict()
    deleted_contract = Contract.objects.get(id=contract_id)
    if request.method == 'GET':
        data['contract'] = deleted_contract
        return render(request, 'contractbase/delcontract.html', context=data)
    elif request.method == 'POST':
        deleted_contract.delete()
        return redirect('/contractbase/index')


def addcontract(request):
    data = dict()
    if request.method == 'GET':
        # блокировка доступа через ад строку
        if request.user.username == 'Deosz':
            data['form'] = ContractForm()
            return render(request, 'contractbase/addcontract.html', context=data)
        else:
            return render(request, 'layouts/page403.html')
    elif request.method == 'POST':
        # обработка данных формы добавления новости
        field_form = ContractForm(request.POST)
        field_form.save()
        return redirect('/contractbase/index')
