# Generated by Django 4.2.19 on 2025-02-23 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0005_author_remove_book_publication_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(default=2000),
        ),
    ]
