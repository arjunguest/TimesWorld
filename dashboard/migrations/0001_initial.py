# Generated by Django 4.2.2 on 2023-09-13 12:12

from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('student', 'Student'), ('staff', 'Staff'), ('editor', 'Editor'), ('admin', 'Admin')], default='student', max_length=20)),
                ('country', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
