# Generated by Django 5.1.1 on 2024-09-29 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0008_alter_income_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Income',
        ),
    ]