# Generated by Django 4.0.2 on 2022-03-16 05:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0002_sredmodel_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='sredmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 16, 5, 42, 0, 516330, tzinfo=utc), verbose_name='掲示板作成日時'),
        ),
        migrations.AddField(
            model_name='sredmodel',
            name='delete_flg',
            field=models.BooleanField(default=False, help_text='削除されたらTrue', verbose_name='掲示板削除フラグ'),
        ),
        migrations.AddField(
            model_name='sredmodel',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='編集日時'),
        ),
        migrations.CreateModel(
            name='Sred_msg_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_detail', models.CharField(max_length=255, verbose_name='メッセージ内容')),
                ('msg_author', models.CharField(max_length=50)),
                ('create_at', models.DateTimeField(default=datetime.datetime(2022, 3, 16, 5, 42, 0, 527300, tzinfo=utc), verbose_name='メッセージ送信日時')),
                ('delete_flg', models.BooleanField(default=False, help_text='削除されたらTrue', verbose_name='メッセージ削除フラグ')),
                ('sred', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boardapp.sredmodel')),
            ],
        ),
    ]
