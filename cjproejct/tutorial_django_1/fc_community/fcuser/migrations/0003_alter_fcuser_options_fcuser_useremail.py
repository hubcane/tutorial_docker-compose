# Generated by Django 4.1 on 2022-08-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fcuser", "0002_alter_fcuser_username"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="fcuser",
            options={"verbose_name": "패스트캠퍼스 사용자", "verbose_name_plural": "패스트캠퍼스 사용자"},
        ),
        migrations.AddField(
            model_name="fcuser",
            name="useremail",
            field=models.CharField(
                default="test@gmail.com", max_length=50, verbose_name="이메일"
            ),
            preserve_default=False,
        ),
    ]