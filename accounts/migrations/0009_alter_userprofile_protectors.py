# Generated by Django 5.0.7 on 2024-07-21 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_userprofile_protectors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='protectors',
            field=models.ManyToManyField(related_name='seniors', to='accounts.userprofile'),
        ),
    ]
