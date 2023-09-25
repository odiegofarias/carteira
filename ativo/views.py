from django.shortcuts import render, redirect
from .models import Ativo, Corretora
from .forms import AtivoForm
from django.db.models import Sum, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
import json


def get_cotacao(ticker):
    url = f'https://brapi.dev/api/quote/{ticker}'
    response = requests.get(url)
    data = json.loads(response.content)

    return data['results'][0]['regularMarketPrice']



def index(request):
    movimentacoes = Ativo.objects.all().order_by('-criado_em')


    # valores_aplicados = Ativo.objects.values('ativo').annotate(
    #     total=Sum(
	#         F('valor_unitario') * F('quantidade')
    #     )
    # )

    # ativos = Ativo.objects.all()

    # print(valores_aplicados)
    # # print(ativos)

    

    return render(request, 'index.html', {'movimentacoes': movimentacoes})
    

def ativo(request):

    return redirect('index')


def add(request):
    form = AtivoForm()

    if request.method == "POST":
        form = AtivoForm(request.POST)

        form.save()

        return redirect('index')
    

    return render(request, 'add.html', {'form': form})

def delete(request, pk):
    movimentacao = Ativo.objects.get(id=pk)

    if request.method == "POST":
        movimentacao.delete()

    return redirect('index')
    

