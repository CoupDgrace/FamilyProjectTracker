# Generated by Django 3.2 on 2021-05-18 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memberName', models.CharField(max_length=15)),
                ('memberSquad', models.CharField(max_length=15)),
                ('memberIsAssignedTask', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=25)),
                ('taskParent', models.IntegerField()),
                ('taskCreatedDateTime', models.DateTimeField(auto_now_add=True)),
                ('taskDeadline', models.DateTimeField()),
                ('taskPriority', models.IntegerField()),
                ('taskHasChild', models.BooleanField()),
                ('taskStatus', models.CharField(max_length=10)),
                ('taskPercentComplete', models.SmallIntegerField()),
                ('assignedMember', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='FTM.members')),
            ],
        ),
        migrations.CreateModel(
            name='taskNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noteContent', models.CharField(max_length=500)),
                ('noteDateTime', models.DateTimeField(auto_now=True)),
                ('memberName', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='FTM.members')),
                ('taskTitle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='FTM.tasks')),
            ],
        ),
    ]
