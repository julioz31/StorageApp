# Generated by Django 5.1.6 on 2025-03-15 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suppliers',
            name='po_batkovi',
            field=models.CharField(default='SOME STRING', max_length=255),
        ),
        migrations.AddField(
            model_name='suppliers',
            name='surname',
            field=models.CharField(default='SOME STRING', max_length=255),
        ),
    ]
