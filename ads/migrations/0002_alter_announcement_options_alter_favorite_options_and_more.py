# Generated by Django 4.1.7 on 2023-04-01 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="announcement",
            options={
                "ordering": ["author__username"],
                "verbose_name": "Объявление",
                "verbose_name_plural": "Объявления",
            },
        ),
        migrations.AlterModelOptions(
            name="favorite",
            options={"verbose_name": "Избранное", "verbose_name_plural": "Избранные"},
        ),
        migrations.AlterField(
            model_name="announcement",
            name="image",
            field=models.ImageField(
                null=True, upload_to="images", verbose_name="Добавить фото"
            ),
        ),
    ]
