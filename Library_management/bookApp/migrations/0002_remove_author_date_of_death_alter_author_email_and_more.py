# Generated by Django 4.2.1 on 2023-05-14 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='date_of_death',
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_added',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('FICTION', 'FIC'), ('POLITICS', 'POL'), ('FINANCE', 'FIN'), ('ROMANCE', 'ROM')], max_length=15),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('YORUBA', 'Y'), ('HAUSA', 'H'), ('IGBO', 'I'), ('ENGLISH', 'E')], max_length=15),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'A'), ('BORROWED', 'B')], default='A', max_length=15),
        ),
    ]