# Generated by Django 4.2.6 on 2023-10-11 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_name_menuitem_menu_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.menuitem'),
        ),
    ]
