# Generated by Django 2.0.4 on 2018-04-11 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_auto_20180411_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='blog/article/static/article/images/%Y/%m/%d', verbose_name='Картинка'),
        ),
    ]
