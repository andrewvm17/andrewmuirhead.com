# Generated by Django 4.0.3 on 2022-03-17 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='asd', max_length=255),
            preserve_default=False,
        ),
    ]
