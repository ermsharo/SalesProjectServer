# Generated by Django 4.2.6 on 2023-10-16 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sales_server", "0004_alter_sale_client_remove_sale_product_list_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client_agent",
            name="telephone",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="seller_agent",
            name="telephone",
            field=models.CharField(max_length=256),
        ),
    ]
