# Generated by Django 3.0.5 on 2020-05-09 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200509_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='category',
            field=models.CharField(choices=[('M', 'Motors'), ('CSA', 'Clothing, Shoes & Accessories'), ('B', 'Books'), ('PS', 'Pet Supplies'), ('BI', 'Business & Industrial'), ('DB', 'Dolls & Bears'), ('SG', 'Sporting Goods'), ('CE', 'Consumer Electronics'), ('C', 'Crafts'), ('CTN', 'Computers/Tablets & Networking'), ('TH', 'Toys & Hobbies'), ('A', 'Antiques'), ('SCF', 'Sports Mem, Cards & Fan Shop'), ('HG', 'Home & Garden')], max_length=3),
        ),
        migrations.AlterField(
            model_name='advert',
            name='posted',
            field=models.DateTimeField(blank=True, default='2020-05-10 00:16:42', null=True),
        ),
        migrations.AlterField(
            model_name='advertcomments',
            name='advert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Advert'),
        ),
        migrations.AlterField(
            model_name='advertcomments',
            name='date',
            field=models.DateTimeField(blank=True, default='2020-05-10 00:16:42', null=True),
        ),
        migrations.AlterField(
            model_name='bought',
            name='date',
            field=models.DateTimeField(blank=True, default='2020-05-10 00:16:42', null=True),
        ),
    ]
