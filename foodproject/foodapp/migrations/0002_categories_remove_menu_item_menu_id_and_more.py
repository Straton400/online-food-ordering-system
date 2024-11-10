# Generated by Django 5.1 on 2024-09-07 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='menu_item',
            name='menu_id',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='customer_id',
        ),
        migrations.DeleteModel(
            name='menu',
        ),
        migrations.DeleteModel(
            name='menu_item',
        ),
        migrations.DeleteModel(
            name='orders',
        ),
    ]