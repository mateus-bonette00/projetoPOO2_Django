# Generated by Django 4.2.2 on 2023-06-29 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itacar_app', '0002_avaliacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricoViagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDMotorista', models.CharField(max_length=100)),
                ('IDpassageiro', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('horario', models.TimeField()),
                ('valorViagem', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
