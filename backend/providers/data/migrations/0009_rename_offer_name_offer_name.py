# Generated by Django 4.1.7 on 2023-03-10 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_offer_offer_name_alter_offer_plans'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='offer_name',
            new_name='name',
        ),
    ]
