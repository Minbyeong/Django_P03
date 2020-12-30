# Generated by Django 3.1.4 on 2020-12-27 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_auto_20201227_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
                ('high', models.IntegerField(blank=True, db_column='High', null=True)),
                ('low', models.IntegerField(blank=True, db_column='Low', null=True)),
                ('open', models.IntegerField(blank=True, db_column='Open', null=True)),
                ('close', models.IntegerField(blank=True, db_column='Close', null=True)),
                ('volume', models.IntegerField(blank=True, db_column='Volume', null=True)),
                ('adj_close', models.IntegerField(blank=True, db_column='Adj Close', null=True)),
            ],
            options={
                'db_table': 'apple',
                'ordering': ['-date'],
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Aapl',
        ),
    ]