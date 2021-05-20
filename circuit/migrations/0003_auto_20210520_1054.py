# Generated by Django 3.1 on 2021-05-20 05:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('circuit', '0002_auto_20210519_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer_name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('product_code', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=500, null=True)),
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
                ('altitude', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=255)),
                ('site_survey_status', models.CharField(choices=[('Not Initiated', 'Not Initiated'), ('Initiated', 'Initiated'), ('Completed', 'Completed')], default='Not Initiated', max_length=100)),
                ('project_status', models.CharField(choices=[('Not Initiated', 'Not Initiated'), ('Initiated', 'Initiated'), ('Completed', 'Completed'), ('Rejected', 'Rejected')], default='Not Initiated', max_length=100)),
                ('circuit_id', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'Opportunities',
                'db_table': 'opportunities',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProductDirectory',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_name', models.CharField(max_length=500)),
                ('region', models.CharField(default='NG', max_length=20)),
                ('product_code', models.CharField(max_length=10)),
                ('number_prefix', models.CharField(default='0', max_length=3)),
            ],
            options={
                'verbose_name': 'Product Directory',
                'db_table': 'product_directory',
            },
        ),
        migrations.AlterField(
            model_name='productcircuit',
            name='id',
            field=models.IntegerField(default=1),
        ),
    ]