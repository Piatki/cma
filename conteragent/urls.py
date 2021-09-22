from django.urls import path
from . import views

app_name = 'conteragent'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('addlpu/', views.addlpu, name='addlpu'),
    path('editlpu/<int:lpu_id>', views.editlpu, name='editlpu'),
    path('dellpu/<int:lpu_id>', views.dellpu, name='dellpu')
]