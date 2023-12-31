# Generated by Django 4.2.6 on 2023-12-04 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paciente', '0001_initial'),
        ('medicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('idAgendamento', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateTimeField()),
                ('motivo', models.CharField(max_length=255)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicos.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente')),
            ],
        ),
    ]
