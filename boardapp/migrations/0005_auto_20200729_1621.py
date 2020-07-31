# Generated by Django 2.2.6 on 2020-07-29 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0004_auto_20200729_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='djangoboard',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='djangoboard',
            name='content',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='djangoboard',
            name='created_date',
            field=models.DateField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='djangoboard',
            name='subject',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
