from django.db import models

# Create your models here.
from django.contrib.gis.db import models

class Country(models.Model):
    iso_code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=100)
    geometry = models.MultiPolygonField()
    
    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name
    
class WorldBorder(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    fips = models.CharField(max_length=2,null=True)
    iso2 = models.CharField("2 Digit ISO", max_length=2)
    iso3 = models.CharField("3 Digit ISO", max_length=3)
    pop2005 = models.BigIntegerField("Population 2005")
    un = models.IntegerField("United Nations Code")
    region = models.IntegerField("Region Code")
    subregion = models.IntegerField("Sub-Region Code")
    
    
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

# Auto-generated `LayerMapping` dictionary for WorldBorder model
worldborder_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'geom': 'MULTIPOLYGON',
}