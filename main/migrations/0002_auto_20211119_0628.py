# Generated by Django 3.2.9 on 2021-11-19 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('person', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('occasion', models.CharField(blank=True, max_length=50)),
                ('special_request', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Table Book',
                'verbose_name_plural': 'Table Books',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='labels',
            field=models.CharField(blank=True, choices=[('BestSeller', 'BestSeller'), ('New', 'New'), ('Spicy🔥', 'Spicy🔥')], max_length=25),
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('ordered_date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Delivered', 'Delivered')], default='Active', max_length=20)),
                ('delivery_date', models.DateField(default=django.utils.timezone.now)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cart Item',
                'verbose_name_plural': 'Cart Items',
            },
        ),
    ]
