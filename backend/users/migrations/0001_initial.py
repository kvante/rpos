# Generated by Django 3.1.7 on 2021-03-31 16:53

import django.core.validators
from django.db import migrations, models
import users.models.custom_user


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message="Телефон должен быть в формате: '+375296788767'", regex='^\\+?1?\\d{9,15}$')], verbose_name='Телефонный номер')),
                ('is_student', models.BooleanField(default=False, verbose_name='Студент')),
                ('is_teacher', models.BooleanField(default=False, verbose_name='Преподаватель')),
                ('is_partner', models.BooleanField(default=False, verbose_name='Партнер')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Сотрудник')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Админ')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Все пользователи',
            },
            managers=[
                ('objects', users.models.custom_user.UserManager()),
            ],
        ),
    ]