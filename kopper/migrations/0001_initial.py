# Generated by Django 2.0.6 on 2018-06-09 22:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deployment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('host', models.CharField(editable=False, max_length=128)),
                ('image', models.CharField(editable=False, max_length=128)),
                ('tag', models.CharField(editable=False, max_length=128)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]