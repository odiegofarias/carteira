from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.ativo, name='ativo'),
    path('add/', views.add, name='add'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
