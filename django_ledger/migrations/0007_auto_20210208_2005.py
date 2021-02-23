# Generated by Django 3.1.4 on 2021-02-09 01:05

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import mptt.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('django_ledger', '0006_auto_20210118_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledgermodel',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='Hidden Ledger'),
        ),
        migrations.AlterField(
            model_name='ledgermodel',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ledgers', to='django_ledger.entitymodel', verbose_name='Ledger Entity'),
        ),
        migrations.AlterField(
            model_name='ledgermodel',
            name='locked',
            field=models.BooleanField(default=False, verbose_name='Locked Ledger'),
        ),
        migrations.AlterField(
            model_name='ledgermodel',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Ledger Name'),
        ),
        migrations.AlterField(
            model_name='ledgermodel',
            name='posted',
            field=models.BooleanField(default=False, verbose_name='Posted Ledger'),
        ),
        migrations.CreateModel(
            name='EntityUnitModel',
            fields=[
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField()),
                ('active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('hidden', models.BooleanField(default=False, verbose_name='Is Hidden')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_ledger.entitymodel', verbose_name='Unit Entity')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='django_ledger.entityunitmodel', verbose_name='Parent Unit')),
            ],
            options={
                'verbose_name': 'Entity Unit Model',
                'ordering': ['-created'],
                'abstract': False,
            },
            managers=[
                ('_tree_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='ledgermodel',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='django_ledger.entityunitmodel', verbose_name='Associated Entity Unit'),
        ),
        migrations.AddIndex(
            model_name='entityunitmodel',
            index=models.Index(fields=['active'], name='django_ledg_active_2c2caa_idx'),
        ),
        migrations.AddIndex(
            model_name='entityunitmodel',
            index=models.Index(fields=['hidden'], name='django_ledg_hidden_a01d42_idx'),
        ),
        migrations.AddIndex(
            model_name='entityunitmodel',
            index=models.Index(fields=['entity'], name='django_ledg_entity__0bdfdc_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='entityunitmodel',
            unique_together={('entity', 'slug')},
        ),
    ]