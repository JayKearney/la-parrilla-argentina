from django.db import models
from django.utils.text import slugify

# Create your models here.


class Meats(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    people = models.IntegerField()
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    preparation_time = models.IntegerField()
    image = models.ImageField(upload_to='menu/')
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args , **kwargs):
        if not self.slug and self.name :
            self.slug = slugify(self.name)
        super(Meats, self).save(*args , **kwargs)

    
    def __str__(self):
        return self.name

    
    class Meta: 
        verbose_name = 'meat'
        verbose_name_plural = 'meats'

