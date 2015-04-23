from django.db import models
#from django.contrib.gis.db.models.manager import GeoManager
#from django.contrib.gis.db.models import PointField


class Company(models.Model):
    user = models.ForeignKey('accounts.User',
                             related_name='companies')
    name = models.CharField(max_length=100)
    # And more... ;)


class Office(models.Model):
    company = models.ForeignKey('Company',
                                related_name='offices')
    name = models.CharField(max_length=100)
    #geo = PointField(help_text=_("(longitude, latitude)"), null=True, blank=True) # TODO uncomment it when add posgres
    address = models.CharField(max_length=200)  # TODO mb separated model for this


class Room(models.Model):
    office = models.ForeignKey('Office',
                               related_name='rooms')
    number = models.IntegerField()
    name = models.CharField(max_length=100)  # optional
    metrage = models.IntegerField()


class Desk(models.Model):
    room = models.ForeignKey('Room',
                             related_name='desks')
    actual_owner = models.OneToOneField('accounts.User',
                                        related_name='desk',
                                        null=True)
    rent_start_date = models.DateTimeField(null=True)
    rent_end_date = models.DateTimeField(null=True)
    number = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    height = models.IntegerField()
    color = models.IntegerField()  # Add mb color choices
    price = models.IntegerField()  # In EUR/Hour  # TODO action set price to many desks
    # TODO add image mb