# Generated by Django 3.1.7 on 2021-03-19 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20210318_1624'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('can_edit_author', 'Add, update or delete author'),)},
        ),
    ]