from django.urls import path

from alurareceitas.receitas import views

urlpatterns = [
    path('', views.index, name='index')
]
