# Generated by Django 3.1.2 on 2020-11-10 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_talk'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talk',
            options={'verbose_name': 'talk', 'verbose_name_plural': 'talks'},
        ),
        migrations.AlterField(
            model_name='talk',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='talk',
            name='speakers',
            field=models.ManyToManyField(blank=True, to='core.Speaker'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='start',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
