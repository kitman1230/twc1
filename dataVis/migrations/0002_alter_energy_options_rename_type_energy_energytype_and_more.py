# Generated by Django 4.2.7 on 2023-11-05 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataVis', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='energy',
            options={'ordering': ('energyYear', 'energyType')},
        ),
        migrations.RenameField(
            model_name='energy',
            old_name='type',
            new_name='energyType',
        ),
        migrations.RenameField(
            model_name='energy',
            old_name='year',
            new_name='energyYear',
        ),
    ]
