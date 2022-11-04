from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now = True)
    slug = models.SlugField(max_length = 200, unique = True)
    image = models.ImageField(null = True, 
                              blank = True, 
                              upload_to = "image/")

#slugify 
def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.title)
    super.save(*args, **kwargs)