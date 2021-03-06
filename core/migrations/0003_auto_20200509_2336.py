# Generated by Django 3.0.5 on 2020-05-09 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200509_0120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertcomments',
            old_name='buyer',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='advert',
            name='category',
            field=models.CharField(choices=[('BI', 'Business & Industrial'), ('SCF', 'Sports Mem, Cards & Fan Shop'), ('HG', 'Home & Garden'), ('TH', 'Toys & Hobbies'), ('C', 'Crafts'), ('DB', 'Dolls & Bears'), ('PS', 'Pet Supplies'), ('A', 'Antiques'), ('SG', 'Sporting Goods'), ('CE', 'Consumer Electronics'), ('M', 'Motors'), ('CTN', 'Computers/Tablets & Networking'), ('B', 'Books'), ('CSA', 'Clothing, Shoes & Accessories')], max_length=3),
        ),
        migrations.AlterField(
            model_name='advert',
            name='posted',
            field=models.DateTimeField(blank=True, default='2020-05-09 23:36:53', null=True),
        ),
        migrations.AlterField(
            model_name='advertcomments',
            name='date',
            field=models.DateTimeField(blank=True, default='2020-05-09 23:36:53', null=True),
        ),
        migrations.AlterField(
            model_name='bought',
            name='date',
            field=models.DateTimeField(blank=True, default='2020-05-09 23:36:53', null=True),
        ),
    ]
