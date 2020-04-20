# Generated by Django 3.0.4 on 2020-04-07 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0005_menu_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant_Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Cuisine')),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Item_Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Cuisine')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Cuisine')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Customer')),
            ],
        ),
    ]