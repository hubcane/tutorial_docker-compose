# Generated by Django 4.1 on 2022-08-30 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tag", "0001_initial"),
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="tags",
            field=models.ManyToManyField(to="tag.tag", verbose_name="태그"),
        ),
    ]