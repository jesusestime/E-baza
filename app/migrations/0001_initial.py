# Generated by Django 4.1.6 on 2023-04-28 04:18

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nom')),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='Nom')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=45)),
                ('name', models.CharField(default='Non spécifié', max_length=45, verbose_name='Nom')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nom')),
                ('commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.commune', verbose_name='Commune')),
            ],
        ),
        migrations.CreateModel(
            name='Trimestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='Nom')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.theme', verbose_name='Thème')),
            ],
        ),
        migrations.CreateModel(
            name='Fiche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(choices=[('10-14 ans', '10-14 ans'), ('15-19 ans', '15-19 ans'), ('20-24 ans', '20-24 ans')], max_length=45, verbose_name="Tranche d'age")),
                ('sexe', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=45, verbose_name='Sexe')),
                ('nombre', models.IntegerField(default=0, verbose_name="Nombre d'individus")),
                ('institutions', models.CharField(max_length=45, verbose_name='Institutions')),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.centre', verbose_name='Centre')),
                ('commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.commune', verbose_name='Commune')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.theme', verbose_name='Thème')),
                ('trimestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trimestre', verbose_name='Trimestre')),
            ],
        ),
        migrations.AddField(
            model_name='centre',
            name='trimestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trimestre', verbose_name='Trimestre'),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(default='default.jpg', upload_to='profile_images', verbose_name='Avatar')),
                ('registration_number', models.CharField(max_length=45, verbose_name='Numéro de matricule')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='Date de naissance')),
                ('sex', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=10, verbose_name='Sexe')),
                ('tel', models.CharField(max_length=45, verbose_name='Téléphone')),
                ('address', models.CharField(max_length=45, verbose_name='Adresse')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.employee_service', verbose_name='Service employé')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
