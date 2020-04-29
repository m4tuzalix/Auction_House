from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    title = models.CharField(max_length = 100)
    category = models.CharField(choices=Advert_Categories, max_length=3)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField(max_length = 1000)
    image = models.ImageField(blank=True, upload_to="advert_images")

    def __str__(self):
        return f"{self.user} advert"
    
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



