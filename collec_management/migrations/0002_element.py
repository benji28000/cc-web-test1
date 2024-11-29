# Generated by Django 5.1.1 on 2024-11-29 21:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collec_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('value', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('collec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elements', to='collec_management.collec')),
            ],
        ),
    ]