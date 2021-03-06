# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('message', models.TextField(max_length=140)),
                ('matcher', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryActionCriteria',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('order', models.IntegerField()),
                ('should_have', models.BooleanField(default=True)),
                ('error_message', models.TextField(max_length=140)),
                ('action', models.ForeignKey(to='mud_backend.Action')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryActionResult',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('should_have', models.BooleanField(default=True)),
                ('message', models.TextField(max_length=140)),
                ('action', models.ForeignKey(to='mud_backend.Action')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('description', models.TextField(max_length=140)),
                ('can_inventory', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('description', models.TextField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='RoomActionResult',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('action', models.ForeignKey(to='mud_backend.Action')),
                ('room', models.ForeignKey(to='mud_backend.Room')),
            ],
        ),
        migrations.CreateModel(
            name='SaveSlot',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('key', models.CharField(max_length=64)),
                ('value', models.CharField(max_length=256)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SaveSlotActionCriteria',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('order', models.IntegerField()),
                ('key', models.CharField(max_length=64)),
                ('value', models.CharField(max_length=256)),
                ('error_message', models.TextField(max_length=140)),
                ('action', models.ForeignKey(to='mud_backend.Action')),
            ],
        ),
        migrations.CreateModel(
            name='SaveSlotActionResult',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('key', models.CharField(max_length=64)),
                ('value', models.CharField(max_length=256)),
                ('message', models.TextField(max_length=140)),
                ('action', models.ForeignKey(to='mud_backend.Action')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('room', models.ForeignKey(to='mud_backend.Room')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='inventoryactionresult',
            name='item',
            field=models.ForeignKey(to='mud_backend.Item'),
        ),
        migrations.AddField(
            model_name='inventoryactioncriteria',
            name='item',
            field=models.ForeignKey(to='mud_backend.Item'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='item',
            field=models.ForeignKey(to='mud_backend.Item'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='action',
            name='room',
            field=models.ForeignKey(to='mud_backend.Room'),
        ),
    ]
