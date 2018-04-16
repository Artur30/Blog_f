# Generated by Django 2.0.4 on 2018-04-16 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0033_auto_20180416_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_author',
            field=models.CharField(default='Гумиров Артур (artur)', max_length=200, verbose_name='Автор статьи'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='article_start_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/article/%Y/%m/%d', verbose_name='Начальная картинка'),
        ),
    ]
