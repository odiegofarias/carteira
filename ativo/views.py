from django.shortcuts import render


def index(request):
    # ativos = Ativo.objects.values('nome').annotate(total=Sum('valor_aplicado')).order_by('nome')

    
    return render(request, 'index.html', {'ativos': ativos})
