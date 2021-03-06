# Generated by Django 4.0.2 on 2022-02-28 00:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_fname', models.CharField(max_length=50)),
                ('cust_lname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('buying_time', models.DateTimeField()),
                ('price_range_min', models.CharField(max_length=30)),
                ('price_range_max', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
