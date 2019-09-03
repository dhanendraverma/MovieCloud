# Generated by Django 2.2.4 on 2019-09-03 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=200)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('poster', models.ImageField(upload_to='media/image')),
                ('word_cloud', models.ImageField(upload_to='media/image')),
            ],
        ),
    ]
