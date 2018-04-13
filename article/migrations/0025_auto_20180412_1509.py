# Generated by Django 2.0.4 on 2018-04-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0024_auto_20180412_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_file',
            field=models.FileField(blank=True, upload_to='files/article/%Y/%m%d'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='images/article/%Y/%m/%d'),
        ),
    ]
