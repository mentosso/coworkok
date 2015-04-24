from django.db import models
#from django.contrib.gis.db.models.manager import GeoManager
#from django.contrib.gis.db.models import PointField


class Company(models.Model):
    user = models.ForeignKey('accounts.User',
                             related_name='companies')
    name = models.CharField(max_length=100)
    # And more... ;)

    def __unicode__(self):
        return self.name


class DatePriceMixin(models.Model):
    from_date = models.DateTimeField()
    until_date = models.DateTimeField()
    price = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        abstract = True


class Office(DatePriceMixin):
    company = models.ForeignKey('Company',
                                related_name='offices')
    name = models.CharField(max_length=100)
    #geo = PointField(help_text=_("(longitude, latitude)"), null=True, blank=True) # TODO uncomment it when add posgres
    address = models.CharField(max_length=200)  # TODO mb separated model for this

    def __unicode__(self):
        return '%s %s %s' % (self.company, self.name, self.address)


class Room(DatePriceMixin):
    office = models.ForeignKey('Office',
                               related_name='rooms')
    number = models.IntegerField()
    name = models.CharField(max_length=100)  # optional
    metrage = models.IntegerField()

    def __unicode__(self):
        return '%s %s' % (self.office, self.name)


class Desk(DatePriceMixin):
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
    # TODO add image mb

    def __unicode__(self):
        return '%s' % self.room
