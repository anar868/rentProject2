# Generated by Django 3.1.4 on 2021-02-07 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentApp1', '0019_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='not_accepted',
            field=models.BooleanField(default=False),
        ),
    ]