# Generated by Django 3.1.4 on 2021-01-28 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentApp1', '0015_auto_20210128_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elan',
            name='address',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='elan',
            name='comment_count',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='elan',
            name='isFlat',
            field=models.CharField(choices=[('flat', 'Bina evi'), ('apartment', 'Həyət evi')], default='flat', max_length=50),
        ),
    ]
