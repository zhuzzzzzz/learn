# Generated by Django 4.2.11 on 2024-12-19 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='weight',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, help_text='权重高展示顺序靠前', verbose_name='权重'),
        ),
    ]
