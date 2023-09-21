# Generated by Django 4.2.1 on 2023-09-20 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('ssn', models.BigIntegerField(unique=True)),
                ('email', models.EmailField(max_length=2550, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('phone_number', models.BigIntegerField()),
                ('profile_picture', models.BinaryField(blank=True, editable=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=70)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CityDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactedReferrer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('position', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('observation', models.TextField(blank=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.division')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.citydepartment')),
            ],
        ),
        migrations.CreateModel(
            name='Mayor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.location')),
            ],
        ),
        migrations.CreateModel(
            name='PoliticParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RequestStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VehicleBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='VehiclePlate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='VisitStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Why',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('finish_time', models.TimeField()),
                ('flyer', models.BooleanField()),
                ('rent_observations', models.TextField()),
                ('distance', models.IntegerField()),
                ('travel_time', models.TimeField()),
                ('civil_registration', models.BooleanField()),
                ('place_name', models.CharField(max_length=70)),
                ('accommodation', models.BooleanField()),
                ('modernization_fund', models.BooleanField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.address')),
                ('agreement', models.ManyToManyField(to='financiationAPI.agreement')),
                ('contacted_referrer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.contactedreferrer')),
                ('finance_collaborator', models.ManyToManyField(related_name='finance_collaborator', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.group')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.location')),
                ('mayor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='financiationAPI.mayor')),
                ('politic_party', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.politicparty')),
                ('rent_collaborator', models.ManyToManyField(related_name='rent_collaborator', to=settings.AUTH_USER_MODEL)),
                ('visit_status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.visitstatus')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.vehiclebrand')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.vehiclebrand')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.vehiclemodel')),
                ('plate', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.vehicleplate')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_datetime', models.DateTimeField()),
                ('observation', models.TextField(blank=True)),
                ('advisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='financiationAPI.advisor')),
                ('faq', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.faq')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.requeststatus')),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.visit')),
                ('why', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.why')),
            ],
        ),
        migrations.CreateModel(
            name='MayorPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.BigIntegerField()),
                ('mayor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiationAPI.mayor')),
            ],
        ),
        migrations.CreateModel(
            name='MayorEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254)),
                ('mayor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiationAPI.mayor')),
            ],
        ),
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactedReferrerPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.BigIntegerField()),
                ('contacted_referrer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.contactedreferrer')),
            ],
        ),
        migrations.CreateModel(
            name='ContactedReferrerEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254)),
                ('contacted_referrer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.contactedreferrer')),
            ],
        ),
        migrations.AddField(
            model_name='advisor',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.group'),
        ),
        migrations.AddField(
            model_name='advisor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.role'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='user_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='financiationAPI.userstatus'),
        ),
    ]
