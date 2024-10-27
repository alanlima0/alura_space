# Generated by Django 5.1.2 on 2024-10-27 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_fotografia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('ESTRELA', 'Estrela'), ('NEBULOSA', 'Nebulosa'), ('GALAXIA', 'Galáxia'), ('PLANETA', 'Planeta')], default='', max_length=100),
        ),
    ]