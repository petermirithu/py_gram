# Generated by Django 2.2.8 on 2019-12-23 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_comments_imagepost_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagepost',
            options={'ordering': ['image_name']},
        ),
        migrations.AddField(
            model_name='comments',
            name='image_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='insta.ImagePost'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='body',
            field=models.CharField(max_length=1000),
        ),
    ]
