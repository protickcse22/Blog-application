# Generated by Django 2.1 on 2018-08-05 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='dafalut.png', upload_to=''),
        ),
    ]