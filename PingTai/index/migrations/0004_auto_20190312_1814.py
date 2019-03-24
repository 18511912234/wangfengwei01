# Generated by Django 2.1.4 on 2019-03-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('desc', models.CharField(max_length=50, null=True)),
                ('method', models.CharField(default='get', max_length=10)),
                ('url', models.URLField()),
                ('headers', models.TextField(null=True)),
                ('body_type', models.CharField(default='none', max_length=20)),
                ('body_value', models.TextField(null=True)),
                ('checks', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='cases',
            field=models.ManyToManyField(to='index.Cases'),
        ),
    ]