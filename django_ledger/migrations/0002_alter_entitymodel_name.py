# Generated by Django 4.1.3 on 2022-11-22 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ledger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entitymodel',
            name='name',
            field=models.CharField(default='TBD', max_length=150, verbose_name='Entity Name'),
            preserve_default=False,
        ),
    ]