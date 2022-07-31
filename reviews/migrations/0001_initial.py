# Generated by Django 3.0 on 2022-07-30 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the publisher.', max_length=50)),
                ('website', models.URLField(help_text="The Publisher's website.")),
                ('email', models.EmailField(help_text="The publisher's email address.", max_length=254)),
            ],
        ),
    ]