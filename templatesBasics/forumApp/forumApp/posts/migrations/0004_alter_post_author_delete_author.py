# Generated by Django 5.1.1 on 2024-10-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_author_alter_post_content_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
