# Generated by Django 3.1.4 on 2021-02-07 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentApp1', '0021_auto_20210207_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.TextField(default='Hər şey əla idi', max_length=30),
            preserve_default=False,
        ),
    ]
