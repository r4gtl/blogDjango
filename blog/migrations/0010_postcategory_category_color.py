# Generated by Django 4.0.4 on 2022-05-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_fixing_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcategory',
            name='category_color',
            field=models.CharField(default='#FFFFFF', max_length=7),
        ),
    ]
