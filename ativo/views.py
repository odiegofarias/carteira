from django.shortcuts import render, redirect
from .models import Ativo, Corretora
from django.db.models import Sum, F
import requests
import json


def get_cotacao(ticker):
    url = f'https://brapi.dev/api/quote/{ticker}'
    response = requests.get(url)
    data = json.loads(response.content)

    return data['results'][0]['regularMarketPrice']



def index(request):
    ativos = Ativo.objects.values('id', 'ativo', 'corretora__nome', 'quantidade', 'cotacao_atual').annotate(
        total=Sum(
	        F('valor_unitario') * F('quantidade')
        )
    ).order_by('ativo')

    print(ativos)

    
    print(get_cotacao('HGLG11'))

    return render(request, 'index.html', {'ativos': ativos})
    

def ativo(request, id):

    return redirect('index')

