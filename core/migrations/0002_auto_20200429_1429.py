# Generated by Django 3.0.5 on 2020-04-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='category',
            field=models.CharField(choices=[('HG', 'Home & Garden'), ('M', 'Motors'), ('B', 'Books'), ('SCF', 'Sports Mem, Cards & Fan Shop'), ('CTN', 'Computers/Tablets & Networking'), ('BI', 'Business & Industrial'), ('TH', 'Toys & Hobbies'), ('SG', 'Sporting Goods'), ('A', 'Antiques'), ('CE', 'Consumer Electronics'), ('DB', 'Dolls & Bears'), ('CSA', 'Clothing, Shoes & Accessories'), ('PS', 'Pet Supplies'), ('C', 'Crafts')], max_length=3),
        ),
        migrations.AlterField(
            model_name='advert',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
