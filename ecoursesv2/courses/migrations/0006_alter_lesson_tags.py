# Generated by Django 4.1 on 2022-09-02 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_rename_create_date_course_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='lessons', to='courses.tag'),
        ),
    ]
