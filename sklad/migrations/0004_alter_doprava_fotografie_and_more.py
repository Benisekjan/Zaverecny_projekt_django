# Generated by Django 4.0.3 on 2024-06-09 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0003_alter_dodavatele_fotografie_alter_doprava_fotografie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doprava',
            name='fotografie',
            field=models.ImageField(blank=True, null=True, upload_to='dopravci', verbose_name='Fotografie'),
        ),
        migrations.AlterField(
            model_name='zakaznici',
            name='telefon_zakaznik',
            field=models.CharField(help_text='Zadejte telefon', max_length=13, unique=True, verbose_name='Telefon zákazníka'),
        ),
    ]