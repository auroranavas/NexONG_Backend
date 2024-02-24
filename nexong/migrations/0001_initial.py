# Generated by Django 5.0.2 on 2024-02-23 21:06

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('capacity', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Educator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(default=600000000, validators=[django.core.validators.MaxValueValidator(999999999), django.core.validators.MinValueValidator(600000000)])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('educator_ID', models.CharField(max_length=9, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('gradeSystem', models.CharField(choices=[('ZERO_TO_ONE', '0-1'), ('ONE_TO_FIVE', '1-5'), ('ZERO_TO_TEN', '0-10')], default='ZERO_TO_TEN', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent_ID', models.CharField(max_length=9, unique=True)),
                ('phone', models.IntegerField(default=600000000, validators=[django.core.validators.MaxValueValidator(999999999), django.core.validators.MinValueValidator(600000000)])),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('date', models.DateField(blank=True)),
                ('time', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holder', models.CharField(max_length=50, unique=True)),
                ('iban', models.CharField(max_length=34, unique=True)),
                ('quantity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('frecuency', models.CharField(choices=[('ANNUAL', 'Anual'), ('MENSUAL', 'Mensual'), ('QUARTERLY', 'Trimestral'), ('SIX-MONTHLY', ' Seis Meses')], default='MENSUAL', max_length=11)),
                ('phone', models.IntegerField(default=600000000, validators=[django.core.validators.MaxValueValidator(999999999), django.core.validators.MinValueValidator(600000000)])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('partner_ID', models.CharField(max_length=9, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('enrollment_document', models.FileField(upload_to='')),
                ('quota_extension_document', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_formation', models.CharField(max_length=1000)),
                ('motivation', models.CharField(max_length=1000)),
                ('status', models.CharField(choices=[('PENDING', 'Pendiente'), ('ACCEPTED', 'Aceptado'), ('REJECTED', 'Rechazado')], default='PENDING', max_length=10)),
                ('phone', models.IntegerField(default=600000000, validators=[django.core.validators.MaxValueValidator(999999999), django.core.validators.MinValueValidator(600000000)])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('postal_code', models.IntegerField(default=10000, validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(90000)])),
                ('inscription_document', models.FileField(upload_to='')),
                ('registry_sheet', models.FileField(upload_to='')),
                ('sexual_offenses_document', models.FileField(upload_to='')),
                ('scanned_volunteer_id', models.FileField(upload_to='')),
                ('minor_authorization', models.FileField(upload_to='')),
                ('scanned_authorizer_id', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('place', models.CharField(max_length=1000)),
                ('capacity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('max_volunteers', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('start_date', models.DateTimeField(blank=True)),
                ('end_date', models.DateTimeField(blank=True)),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nexong.class')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educative_centre', models.CharField(max_length=100)),
                ('educative_centre_tutor', models.CharField(max_length=50)),
                ('current_education_year', models.CharField(choices=[('THREE_YEARS', 'Tres años'), ('FOUR_YEARS', 'Cuatro años'), ('FIVE_YEARS', 'Cinco años'), ('FIRST_PRIMARY', 'Primero de primaria'), ('SECOND_PRIMARY', 'Segundo de primaria'), ('THIRD_PRIMARY', 'Tercero de primaria'), ('FOURTH_PRIMARY', 'Cuarto de primaria'), ('FIFTH_PRIMARY', 'Quinto de primaria'), ('SIXTH_PRIMARY', 'Sexto de primaria'), ('FIRST_SECONDARY', 'Primero de secundaria'), ('SECOND_SECONDARY', 'Segundo de secundaria'), ('THIRD_SECONDARY', 'Tercero de secundaria'), ('FOURTH_SECONDARY', 'Cuarto de secundaria')], default='THREE_YEARS', max_length=25)),
                ('enrollment_document', models.FileField(upload_to='')),
                ('scanned_sanitary_card', models.FileField(upload_to='')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexong.family')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=50)),
                ('birthdate', models.DateField(null=True)),
                ('role', models.CharField(choices=[('ADMIN', 'Administrador'), ('VOLUNTEER', 'Voluntario'), ('EDUCATOR', 'Educador'), ('FAMILY', 'Familia'), ('PARTNER', 'Socio'), ('VOLUNTEER_PARTNER', 'Voluntario y socio')], default='FAMILY', max_length=25)),
                ('password', models.CharField(max_length=500)),
                ('avatar', models.URLField(validators=[django.core.validators.URLValidator()])),
                ('address', models.CharField(max_length=255)),
                ('postal_code', models.IntegerField(default=10000, validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(90000)])),
                ('is_active', models.BooleanField(default=False)),
                ('educator', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nexong.educator')),
                ('partner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nexong.partner')),
                ('student', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nexong.student')),
                ('volunteer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nexong.volunteer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('text', models.CharField(max_length=800)),
                ('date_time', models.DateTimeField()),
                ('user_commented', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_commented', to='nexong.user')),
                ('user_who_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_who_comment', to='nexong.user')),
            ],
        ),
        migrations.CreateModel(
            name='Class_Has_Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('date', models.DateField()),
                ('evaluation_type', models.CharField(choices=[('DIARY', 'Diario'), ('ANNUAL', 'Anual')], default='DIARY', max_length=25)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexong.class')),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexong.evaluation')),
                ('user_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexong.user')),
            ],
        ),
        migrations.CreateModel(
            name='Centre_Exit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorization', models.CharField(max_length=100)),
                ('responsible', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexong.user')),
            ],
        ),
        migrations.CreateModel(
            name='User_Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexong.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexong.user')),
            ],
        ),
        migrations.CreateModel(
            name='User_Has_Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexong.class')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexong.user')),
            ],
        ),
        migrations.CreateModel(
            name='User_Has_Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('date', models.DateField()),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexong.evaluation')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexong.class')),
                ('user_educator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_evaluator', to='nexong.user')),
                ('user_evaluated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_evaluated', to='nexong.user')),
            ],
        ),
        migrations.CreateModel(
            name='User_Has_Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexong.meeting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexong.user')),
            ],
        ),
    ]
