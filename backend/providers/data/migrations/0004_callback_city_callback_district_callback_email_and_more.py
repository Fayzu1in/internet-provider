# Generated by Django 4.1.7 on 2023-03-09 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_callback'),
    ]

    operations = [
        migrations.AddField(
            model_name='callback',
            name='city',
            field=models.CharField(default='test', max_length=100, verbose_name='city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='callback',
            name='district',
            field=models.CharField(default='test', max_length=100, verbose_name='district'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='callback',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='callback',
            name='house',
            field=models.CharField(default='test', max_length=100, verbose_name='house'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='callback',
            name='phone',
            field=models.CharField(default='test', max_length=100, verbose_name='phone'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='callback',
            name='street',
            field=models.CharField(default='test', max_length=100, verbose_name='street'),
            preserve_default=False,
        ),
    ]