# Generated by Django 5.0.2 on 2024-02-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_alter_category_options_alter_meal_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='description',
            field=models.TextField(blank=True, default='default_desc', max_length=1000, null=True),
        ),
    ]
