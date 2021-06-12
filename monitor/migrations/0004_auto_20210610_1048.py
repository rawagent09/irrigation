# Generated by Django 3.2.3 on 2021-06-10 05:18

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_auto_20180317_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicestate',
            name='humidity',
        ),
        migrations.AddField(
            model_name='devicecontrol',
            name='lower_threshold',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='devicecontrol',
            name='mode',
            field=models.CharField(choices=[('automated', 'Automated'), ('manual', 'Manual')], default='automated', max_length=10),
        ),
        migrations.AddField(
            model_name='devicecontrol',
            name='upper_threshold',
            field=models.IntegerField(default=500),
        ),
        migrations.AddField(
            model_name='devicestate',
            name='moisture',
            field=models.IntegerField(default=99, verbose_name=builtins.max),
            preserve_default=False,
        ),
    ]