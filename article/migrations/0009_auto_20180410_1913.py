# Generated by Django 2.0.4 on 2018-04-10 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20180410_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='media/article/%Y/%m/%d', verbose_name='Картинка'),
        ),
    ]