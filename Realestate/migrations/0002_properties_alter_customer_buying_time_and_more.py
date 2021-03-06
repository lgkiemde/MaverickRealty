# Generated by Django 4.0.2 on 2022-02-28 01:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Realestate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=10)),
                ('squarefeet', models.IntegerField()),
                ('HeatType', models.CharField(max_length=20)),
                ('ACType', models.CharField(max_length=20)),
                ('garagespaces', models.IntegerField()),
                ('school_districts', models.CharField(max_length=50)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('updated_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='buying_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='customer',
            name='updated_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='LienParcels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=10)),
                ('lot_number', models.CharField(max_length=20)),
                ('block_number', models.CharField(max_length=20)),
                ('acres', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tax_link', models.CharField(max_length=100)),
                ('landvaluation_link', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lien', to='Realestate.properties')),
            ],
        ),
    ]
