# Generated by Django 4.1.7 on 2023-03-10 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='plan',
        ),
        migrations.AddField(
            model_name='offer',
            name='plan',
            field=models.ManyToManyField(to='data.plan', verbose_name='Offer'),
        ),
    ]