# Generated by Django 4.2.16 on 2024-12-03 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0003_stanowisko_osoba'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(auto_now_add=True, default='2024-12-03'),
            preserve_default=False,
        ),
    ]
