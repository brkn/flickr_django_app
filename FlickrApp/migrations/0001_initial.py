# Generated by Django 2.1.4 on 2018-12-25 19:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecentSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=95)),
                ('date_entry', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]