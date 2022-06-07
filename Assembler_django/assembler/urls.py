from django.urls import path
from . import views

app_name = 'assembler'

urlpatterns = [
    path('', views.InputAssembler.as_view(), name='input_assembler'),
    path('output/<str:lines>/', views.OutputAssembler.as_view(), name='output_assembler')
]
