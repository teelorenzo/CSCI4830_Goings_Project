from django.db import models

# Create your models here.

class Venue(models.Model):
    name = models.CharField('Venue Name',max_length=120)
    address = models.CharField('Address',max_length=300)
    zip_code = models.CharField('Zip Code',max_length=15)
    phone = models.CharField('Phone',max_length=120)
    web = models.URLField('Website',blank=True, max_length=120)
    email_address = models.EmailField('Email Address',max_length=120)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField('Event Name',max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, blank=True, null=True)
    manager = models.CharField('Manager of Event',max_length=60)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name