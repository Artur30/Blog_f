# Generated by Django 2.0.4 on 2018-04-15 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0031_article_article_start_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_start_text',
            field=models.TextField(default='Начальный текст', verbose_name='Краткий текст'),
            preserve_default=False,
        ),
    ]
