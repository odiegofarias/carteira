# Generated by Django 4.2.3 on 2023-07-25 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corretora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.CharField(max_length=6)),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=8)),
                ('data_compra', models.DateField()),
                ('taxa', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('cotacao_atual', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('tipo_de_operacao', models.CharField(choices=[('R', 'Retirada'), ('A', 'Aporte')], max_length=1)),
                ('quantidade', models.IntegerField()),
                ('corretora', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ativo.corretora')),
            ],
        ),
    ]
