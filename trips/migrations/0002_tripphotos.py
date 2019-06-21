# Generated by Django 2.2.2 on 2019-06-17 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripPhotos',
            fields=[
                ('trip', models.ForeignKey(db_column='Trip_id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='trips.Trips')),
                ('url', models.TextField(db_column='URL')),
            ],
            options={
                'db_table': "Trip_Photos'",
                'managed': False,
            },
        ),
    ]