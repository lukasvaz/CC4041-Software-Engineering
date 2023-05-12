# Generated by Django 3.1.1 on 2023-05-12 02:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.PositiveBigIntegerField()),
                ('outcome', models.PositiveBigIntegerField()),
                ('actual_balance', models.BigIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Outcomes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outcome', models.PositiveBigIntegerField()),
                ('category', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('set_at', models.DateTimeField()),
                ('account_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.accountstatus')),
            ],
        ),
        migrations.CreateModel(
            name='Incomes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.PositiveBigIntegerField()),
                ('category', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('set_at', models.DateTimeField()),
                ('account_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.accountstatus')),
            ],
        ),
    ]
