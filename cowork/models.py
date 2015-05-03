from __future__ import unicode_literals
from django.db import models


class Company(models.Model):
    user = models.ForeignKey('accounts.User', related_name='companies')
    name = models.CharField(max_length=100)
    VAT_ID = models.CharField(max_length=15, default="")
    website = models.URLField(max_length=50, default="")
    company_logo = models.ImageField(upload_to='company_logos', null=True, blank=True) 

    def __unicode__(self):
        return self.name

    @property
    def image_url(self):
        if self.company_logo and hasattr(self.company_logo, 'url'):
            return self.company_logo.url
        else:
            return '/static/images/default.jpg'


class Location(models.Model):
    company = models.ForeignKey('Company', related_name='locations')
    city = models.CharField(max_length=200, verbose_name='City')
    address = models.CharField(max_length=200, verbose_name='Address')
    postal_code = models.CharField(max_length=6, verbose_name='Postal code')
    total_desks = models.IntegerField(verbose_name='Total desks')
    reserved_desks = models.IntegerField(verbose_name='Reserved desks')
    price = models.DecimalField(verbose_name='Price per desk $', max_digits=12, decimal_places=2)

    def __unicode__(self):
        return '%s' % (self.city)

    @property
    def free_desks(self):
        return self.total_desks - self.reserved_desks


class Desk(models.Model):
    owner = models.OneToOneField('accounts.User', related_name='desks',
        null=True)
    location = models.OneToOneField(Location, related_name='desks', default="")
    rent_start_date = models.DateTimeField(null=True)
    rent_end_date = models.DateTimeField(null=True)

    def __unicode__(self):
        return '%s' % self.location
