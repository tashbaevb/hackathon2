# Generated by Django 4.2.1 on 2023-06-17 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_contractors_remove_review_image_alter_review_rating_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]