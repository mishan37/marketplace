# Generated by Django 2.0.3 on 2018-04-08 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('starting_price', models.IntegerField()),
                ('type_item', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.IntegerField()),
                ('lot_name', models.CharField(max_length=30)),
                ('cost', models.IntegerField()),
                ('item_count', models.IntegerField(null=True)),
                ('user_seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(null=True)),
                ('level', models.IntegerField(null=True)),
                ('country', models.CharField(max_length=50)),
                ('information', models.CharField(max_length=255)),
                ('inventory_status', models.IntegerField()),
                ('inventory_capacity', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_seller_id', models.IntegerField(null=True)),
                ('transaction_date', models.DateTimeField(null=True)),
                ('item_count', models.IntegerField(null=True)),
                ('cost', models.IntegerField(null=True)),
                ('lot_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='marketplace.Lot')),
                ('user_buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Inventory_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.Item')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]