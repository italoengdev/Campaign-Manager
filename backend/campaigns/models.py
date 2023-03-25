from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


class Campaign(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    logo = CloudinaryField('Image', overwrite=True, format="jpg")

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return self.tittle

    def save(self, *args, **kwargs):
        to_asign = slugify(self.tittle)

        if Campaign.objects.filter(slug=to_asign).exists():
            to_asign = to_asign+str(Campaign.objects.all().count())

        self.slug = to_asign

        super().save(*args, **kwargs)


class Subscriber(models.Model):
    email = models.EmailField(max_length=254)
    campaign = models.ForeignKey(Campaign, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return self.email
