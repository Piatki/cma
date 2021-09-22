from django.urls import path
from . import views


app_name = 'clients'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('clientcase/<int:client_id>', views.clientcase, name='clientcase'),
    path('addclient/', views.addclient, name='addclient'),
    path('delclient/<int:client_id>', views.delclient, name='delclient'),
    path('editclient/<int:client_id>', views.editclient, name='editclient'),
    path('clientappeal/', views.clientappeal, name='clientappeal'),
    path('clientcase/<int:client_id>/clientappeal/<int:appeal_id>/formappeal/', views.formappeal, name='formappeal')
]