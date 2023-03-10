# Generated by Django 4.1.4 on 2023-01-15 16:50

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import user_auth.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=40, unique=True, verbose_name='Email')),
                ('company', models.CharField(blank=True, max_length=40, null=True, verbose_name='????????????????')),
                ('position', models.CharField(blank=True, max_length=40, null=True, verbose_name='??????????????????')),
                ('type', models.CharField(choices=[('shop', '??????????????'), ('buyer', '????????????????????')], default='buyer', max_length=5, verbose_name='?????? ????????????????????????')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '????????????????????????',
                'verbose_name_plural': '???????????? ??????????????????????????',
                'ordering': ('email',),
            },
            managers=[
                ('objects', user_auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='??????????')),
                ('street', models.CharField(blank=True, max_length=100, verbose_name='??????????')),
                ('house', models.CharField(blank=True, max_length=35, verbose_name='??????')),
                ('apartment', models.CharField(blank=True, max_length=15, verbose_name='????????????????')),
                ('e_mail', models.EmailField(blank=True, max_length=50, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=35, verbose_name='??????????????')),
                ('work_phone', models.CharField(blank=True, max_length=40, verbose_name='?????????????? ??????????????')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL, verbose_name='????????????????????????')),
            ],
            options={
                'verbose_name': '?????????????? ????????????????????????',
                'verbose_name_plural': '???????????? ?????????????????? ????????????????????????',
            },
        ),
        migrations.CreateModel(
            name='ConfirmEmailToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='When was this token generated')),
                ('key', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='Key')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confirm_email_tokens', to=settings.AUTH_USER_MODEL, verbose_name='The User which is associated to this password reset token')),
            ],
            options={
                'verbose_name': '?????????? ?????????????????????????? Email',
                'verbose_name_plural': '???????????? ?????????????????????????? Email',
            },
        ),
    ]
