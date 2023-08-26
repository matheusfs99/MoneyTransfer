# Generated by Django 4.2.4 on 2023-08-25 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(editable=False, verbose_name='valor')),
                ('payer', models.CharField(editable=False, max_length=255, verbose_name='pagador')),
                ('receiver', models.CharField(editable=False, max_length=255, verbose_name='recebedor')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='data e hora da transação')),
            ],
            options={
                'verbose_name_plural': 'Transactions History',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(default=0, verbose_name='saldo')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]