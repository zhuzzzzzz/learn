# Generated by Django 4.1 on 2024-12-20 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_content_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_html',
            field=models.TextField(blank=True, default=' ', editable=False, verbose_name='正文html代码'),
            preserve_default=False,
        ),
    ]
