from django.shortcuts import render, redirect
from .models import Ativo, Corretora
from .forms import AtivoForm
from django.db.models import Sum, F
import requests
import json


def get_cotacao(ticker):
    url = f'https://brapi.dev/api/quote/{ticker}'
    response = requests.get(url)
    data = json.loads(response.content)

    return data['results'][0]['regularMarketPrice']



def index(request):
    valores_aplicados = Ativo.objects.values('ativo').annotate(
        total=Sum(
	        F('valor_unitario') * F('quantidade')
        )
    )

    ativos = Ativo.objects.all()

    print(valores_aplicados)
    # print(ativos)

    

    return render(request, 'index.html', {'valores_aplicados': valores_aplicados})
    

def ativo(request, id):

    return redirect('index')


def add(request):
    form = AtivoForm

    return render(request, 'add.html', {'form': form})

