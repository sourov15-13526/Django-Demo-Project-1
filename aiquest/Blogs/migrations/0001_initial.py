# Generated by Django 3.0.14 on 2022-04-04 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.IntegerField()),
                ('tname', models.CharField(max_length=40)),
                ('temail', models.EmailField(max_length=50)),
            ],
        ),
    ]
