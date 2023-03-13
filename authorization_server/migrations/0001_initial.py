# Generated by Django 3.1.3 on 2021-04-06 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.BigIntegerField()),
                ('device_name', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RequestCounter',
            fields=[
                ('counter_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('counter', models.IntegerField(default=0)),
                ('last_request_time', models.DateTimeField()),
                ('average', models.FloatField(default=1.0)),
            ],
        ),
        migrations.CreateModel(
            name='ServerMonitoring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overloaded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceGrant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_code', models.BigIntegerField()),
                ('device_name', models.CharField(default='', max_length=30)),
                ('client_id', models.IntegerField()),
                ('user_code', models.IntegerField()),
                ('user_code_lifetime', models.IntegerField(default=1800)),
                ('verification_uri', models.CharField(max_length=50)),
                ('verification_uri_complete', models.CharField(max_length=100)),
                ('interval', models.IntegerField(default=5)),
                ('scope', models.CharField(blank=True, max_length=20, null=True)),
                ('creation_timestamp', models.DateTimeField(auto_now=True)),
                ('authenticated', models.BooleanField(default=False)),
                ('access_token', models.IntegerField(blank=True, null=True)),
                ('access_token_creation_timestamp', models.DateTimeField(blank=True, null=True)),
                ('access_token_lifetime', models.IntegerField(default=604800)),
                ('refresh_token', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authorization_server.user')),
            ],
        ),
    ]
