# Generated by Django 4.1.7 on 2023-03-10 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_remove_offer_plan_offer_plan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='plan',
            new_name='plans',
        ),
    ]
