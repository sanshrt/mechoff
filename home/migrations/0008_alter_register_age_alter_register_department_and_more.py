# Generated by Django 5.0.2 on 2024-11-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_register_department_alter_register_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='age',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='register',
            name='department',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]