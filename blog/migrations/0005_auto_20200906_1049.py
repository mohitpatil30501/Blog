# Generated by Django 3.1 on 2020-09-06 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_likecomment_likepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likecomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.postcomment'),
        ),
        migrations.AlterField(
            model_name='likecomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='likepost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.post'),
        ),
        migrations.AlterField(
            model_name='likepost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]