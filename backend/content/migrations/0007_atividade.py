# Generated by Django 2.2.16 on 2020-10-21 19:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20201018_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id_atividade', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome_ministrante', models.CharField(max_length=200)),
                ('nome_atividade', models.CharField(max_length=200)),
                ('descricao_atividade', models.TextField()),
                ('foto_ministrante', models.ImageField(upload_to='images')),
                ('link', models.URLField(blank=True, null=True)),
                ('tipo_atividade', models.CharField(choices=[('PALESTRA', 'PALESTRA'), ('MINICURSO', 'MINICURSO')], default='PALESTRA', max_length=200)),
            ],
        ),
    ]