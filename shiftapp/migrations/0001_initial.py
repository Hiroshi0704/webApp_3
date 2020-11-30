# Generated by Django 3.1.3 on 2020-11-29 07:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_public', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ShiftApp',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ShiftAppPlan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, unique=True)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('is_manager', models.BooleanField(default=True)),
                ('max_worker', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hourlyWage', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shiftapp.shiftapp')),
                ('worker_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worker_detail', to='shiftapp.shiftapp')),
            ],
        ),
        migrations.CreateModel(
            name='WorkPlan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shiftapp.shiftapp')),
            ],
        ),
        migrations.CreateModel(
            name='WorkStyle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('symbol', models.CharField(max_length=1)),
                ('start_time', models.TimeField()),
                ('break_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('is_night', models.BooleanField(default=False)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shiftapp.shiftapp')),
            ],
        ),
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('is_rest_request', models.BooleanField(default=False)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shiftapp.shiftapp')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shiftapp.shift')),
                ('work_style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shiftapp.workstyle')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shiftapp.worker')),
            ],
        ),
        migrations.CreateModel(
            name='WorkPlanWorkStyleRelation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('work_style_num', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shiftapp.shiftapp')),
                ('work_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shiftapp.workplan')),
                ('work_style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shiftapp.workstyle')),
            ],
        ),
        migrations.CreateModel(
            name='ShiftWorkerRelation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total_time', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shiftapp.shiftapp')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shiftapp.shift')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shiftapp.worker')),
            ],
        ),
        migrations.CreateModel(
            name='ShiftPlan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shiftapp.shiftapp')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shiftapp.shift')),
                ('work_plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shiftapp.workplan')),
            ],
        ),
        migrations.CreateModel(
            name='ShiftAppWorkerInvitation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('expired_by', models.DateField()),
                ('invitee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitee', to='shiftapp.shiftapp')),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inviter', to='shiftapp.shiftapp')),
            ],
        ),
        migrations.AddField(
            model_name='shiftapp',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shiftapp.shiftappplan'),
        ),
        migrations.AddField(
            model_name='shiftapp',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shift',
            name='app',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shiftapp.shiftapp'),
        ),
        migrations.AddField(
            model_name='shift',
            name='worker',
            field=models.ManyToManyField(to='shiftapp.Worker'),
        ),
    ]
