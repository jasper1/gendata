from django.db import models

# Country model
class Country (models.Model):
    country = models.CharField('Country Name', max_length = 100)
    country_code = models.CharField('Country Code', max_length = 2)
    zip_format = models.CharField('ZIP format', max_length = 200, blank=True)
    
    def __unicode__(self):
        return self.country
    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

#Region model
class Region(models.Model):
    country = models.ForeignKey(Country)
    region = models.CharField('Region Name', max_length = 50)
    region_code = models.CharField('Region Code', max_length = 2, blank=True)
    region_short = models.CharField('Region Short Name', max_length = 2, blank=True)
    
    def __unicode__(self):
        return self.region
    
    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'
    
# City model
class City (models.Model):
    country = models.ForeignKey(Country)
    region = models.ForeignKey(Region, blank=True, null=True)
    ASCIIcity = models.CharField('ASCIICity', max_length = 80, null=True)
    city = models.CharField('City', max_length = 80)
    
    population = models.IntegerField('Population', blank=True, null=True)
    latitude = models.FloatField('Latitude', blank=True, null=True) 
    longitude = models.FloatField('Longitude', blank=True, null=True)
    
    def __unicode__(self):
        return self.city

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

# Gender choices
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('B', 'Both'),
    )

# First Name model  
class FirstName(models.Model):
    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES)
    first_name = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return  self.first_name
    
    class Meta:
        verbose_name = 'Name'
        verbose_name_plural = 'Names'
    
class Surname(models.Model):
    surname = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return self.surname
    
    class Meta:
        verbose_name = 'Surname'
        verbose_name_plural = 'Surnames'