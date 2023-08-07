from .models import Ativo
from django import forms


OPERACAO_CHOICES = (
    ('R', 'Retirada'),
    ('A', 'Aporte')
)


class AtivoForm(forms.ModelForm):
    class Meta:
        model = Ativo
        fields = ['tipo_de_operacao', 'ativo', 'corretora', 'valor_unitario', 'data_compra', 'taxa', 'quantidade']
        widgets = {
            'tipo_de_operacao': forms.Select(attrs={'class': 'form-control'}),
            'ativo': forms.TextInput(attrs={'class': 'form-control'}),
            'corretora': forms.Select(attrs={'class': 'form-control'}),
            'valor_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
            'data_compra': forms.DateInput(attrs={'class': 'form-control'}),
            'taxa': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }
