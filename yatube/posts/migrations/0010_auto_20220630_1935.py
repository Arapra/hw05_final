# Generated by Django 2.2.16 on 2022-06-30 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',)},
        ),
    ]