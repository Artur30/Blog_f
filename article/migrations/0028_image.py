# Generated by Django 2.0.4 on 2018-04-13 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0027_auto_20180412_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_img', models.ImageField(blank=True, null=True, upload_to='images/article/%Y/%m/%d', verbose_name='Картинка')),
                ('image_img_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article')),
            ],
            options={
                'db_table': 'image',
            },
        ),
    ]
