# Generated by Django 2.1.5 on 2019-02-05 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('garden_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water', models.CharField(max_length=48)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waterlevel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
