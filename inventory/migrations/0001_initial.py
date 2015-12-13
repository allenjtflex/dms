# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('classify', models.CharField(max_length=4)),
                ('itemcode', models.CharField(max_length=8)),
                ('description', models.CharField(max_length=60)),
                ('is_effective', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('brand_model', models.CharField(max_length=60)),
                ('spec_description', models.TextField()),
                ('purchase_at', models.DateField(auto_now_add=True)),
                ('is_special', models.BooleanField(default=False)),
                ('warranty_month', models.IntegerField(default=1)),
                ('is_effective', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(to='inventory.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Vender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60)),
                ('is_effective', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='equipment',
            name='vender',
            field=models.ForeignKey(to='inventory.Vender'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('classify', 'itemcode')]),
        ),
    ]
