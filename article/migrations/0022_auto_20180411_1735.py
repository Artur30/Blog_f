# Generated by Django 2.0.4 on 2018-04-11 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0021_article_article_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='article/images/%Y/%m/%d', verbose_name='Картинка'),
        ),
    ]
