# Generated by Django 3.1 on 2021-05-19 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circuit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcircuit',
            name='counter',
        ),
        migrations.AlterField(
            model_name='productcircuit',
            name='id',
            field=models.IntegerField(default=1, editable=False),
        ),
        migrations.AlterField(
            model_name='productcircuit',
            name='next_circuit_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
