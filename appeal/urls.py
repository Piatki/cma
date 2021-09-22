from django.urls import path
from . import views


app_name = 'appeal'
urlpatterns = [
    path('clientappeal/', views.clientappeal, name='clientappeal'),
    path('clientcase/<int:client_id>/clientappeal/<int:appeal_id>/formappeal/', views.formappeal, name='formappeal')
]