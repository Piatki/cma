from django.urls import path
from . import views

app_name = 'contractbase'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('contractread/<int:contract_id>', views.contractread, name='contractread'),
    path('editcontract/<int:contract_id>', views.editcontract, name='editcontract'),
    path('delcontract/<int:contract_id>', views.delcontract, name='delcontract'),
    path('addcontract/', views.addcontract, name='addcontract')
]