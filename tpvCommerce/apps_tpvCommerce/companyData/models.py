from django.db import models


class zone(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        db_table = "zone"


class city(models.Model):
    name = models.CharField(max_length=250)
    zone = models.ForeignObject(zone, on_delete=models.CASCADE)

    class Meta:
        db_table = "city"


class dealer(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    rut = models.CharField(max_length=80)
    phone = models.CharField(max_length=30)
    web = models.CharField(max_length=255)
    city = models.ForeignObject(city, on_delete=models.CASCADE)

    class Meta:
        db_table = "dealer"
