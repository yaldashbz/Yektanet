# Generated by Django 3.1 on 2020-11-25 19:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approve',
                 models.CharField(choices=[('accepted', 'قبول'), ('denied', 'رد')], default='denied', max_length=10,
                                  verbose_name='وضعیت')),
                ('title', models.CharField(max_length=100, verbose_name='موضوع')),
                ('img_url', models.URLField(verbose_name=' ادرس عکس تبلیغ')),
                ('link', models.URLField(verbose_name='ادرس سایت شما')),
            ],
            options={
                'verbose_name': 'تبلیغ',
                'verbose_name_plural': 'تبلیغات',
            },
        ),
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='نام')),
            ],
            options={
                'verbose_name': 'تبلیغ کننده',
                'verbose_name_plural': 'تبلیغ کنندگان',
            },
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views',
                                         to='advertiser_management.ad')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('duration', models.DurationField()),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clicks',
                                         to='advertiser_management.ad')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ad',
            name='advertiser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads',
                                    to='advertiser_management.advertiser', verbose_name='تبلیغ کننده'),
        ),
    ]
