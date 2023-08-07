# Generated by Django 4.1.6 on 2023-07-22 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="genre",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="book",
                to="books.genre",
            ),
        ),
    ]