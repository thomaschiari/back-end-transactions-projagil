# Generated by Django 4.0.1 on 2022-10-17 13:51

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
            name='Bank_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=100)),
                ('bank_code', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=100)),
                ('account_name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('1', 'ENTRETENIMENTO'), ('2', 'ALIMENTAÇÃO'), ('3', 'TRANSPORTE'), ('4', 'SAÚDE'), ('5', 'EDUCAÇÃO'), ('6', 'OUTROS')], default='6', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_file', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('document_date', models.DateField()),
                ('total_amount', models.CharField(default=0, max_length=100)),
                ('account', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.bank_account')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(default='Sem Descrição', max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.category')),
                ('document', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.document')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=11)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
