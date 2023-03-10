# Generated by Django 4.1.7 on 2023-03-10 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_rename_offer_name_offer_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('logo', models.ImageField(upload_to='providers/images', verbose_name='')),
            ],
            options={
                'verbose_name': 'TopProvider',
                'verbose_name_plural': 'TopProviders',
            },
        ),
    ]