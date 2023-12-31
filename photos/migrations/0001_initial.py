# Generated by Django 4.2.7 on 2023-11-19 15:38

from django.db import migrations, models
import photos.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('photo', models.ImageField(upload_to=photos.models.folder_based_option)),
                ('category', models.IntegerField(choices=[(1, 'Self'), (0, 'Family'), (2, 'Love')], default=1)),
            ],
        ),
    ]
