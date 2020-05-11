from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator 

Advert_Categories = {
    ("B","Books"),
    ("BI", "Business & Industrial"),
    ("CSA", "Clothing, Shoes & Accessories"),
    ("CE", "Consumer Electronics"),
    ("C", "Crafts"),
    ("DB", "Dolls & Bears"),
    ("HG", "Home & Garden"),
    ("M", "Motors"),
    ("PS", "Pet Supplies"),
    ("SG", "Sporting Goods"),
    ("SCF", "Sports Mem, Cards & Fan Shop"),
    ("TH", "Toys & Hobbies"),
    ("A", "Antiques"),
    ("CTN", "Computers/Tablets & Networking")
}

class Advert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    category = models.CharField(choices=Advert_Categories, max_length=3)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField(max_length = 1000)
    posted = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), blank=True, null=True) 
    image = models.ImageField(blank=True, upload_to="advert_images")
    archive = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super(Advert, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            new_size = (300,300)
            img.thumbnail(new_size)
            img.save(self.image.path)
    
    def absolute_path(self):
        return reverse("advert", kwargs={
            'pk':self.pk,
            'title':self.title
        })
    
    def final_price(self, amount): #// price to pay
        return(int(amount) * self.price)

class Bought(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.FloatField()
    date = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), blank=True, null=True)
    comment = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.advert.title} - {self.date}'

class AdvertComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    advert = models.ForeignKey(Bought, on_delete=models.CASCADE)
    content = models.TextField(max_length = 200)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    date = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), blank=True, null=True) 




