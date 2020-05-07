# Generated by Django 3.0.5 on 2020-05-01 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200429_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='category',
            field=models.CharField(choices=[('M', 'Motors'), ('SCF', 'Sports Mem, Cards & Fan Shop'), ('B', 'Books'), ('CSA', 'Clothing, Shoes & Accessories'), ('DB', 'Dolls & Bears'), ('HG', 'Home & Garden'), ('PS', 'Pet Supplies'), ('TH', 'Toys & Hobbies'), ('C', 'Crafts'), ('BI', 'Business & Industrial'), ('A', 'Antiques'), ('CTN', 'Computers/Tablets & Networking'), ('SG', 'Sporting Goods'), ('CE', 'Consumer Electronics')], max_length=3),
        ),
    ]