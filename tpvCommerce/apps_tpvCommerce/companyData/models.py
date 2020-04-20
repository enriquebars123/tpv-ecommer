from django.db import models


class zone(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        db_table = "zone"

    def __str__(self):
        return self.name


class city(models.Model):
    name = models.CharField(max_length=250)
    zone = models.ForeignKey(zone, on_delete=models.CASCADE)

    class Meta:
        db_table = "city"

    def __str__(self):
        return self.name


class dealer(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    rut = models.CharField(max_length=80)
    phone = models.CharField(max_length=30)
    web = models.CharField(max_length=255)
    city = models.ForeignKey(city, on_delete=models.CASCADE)

    class Meta:
        db_table = "dealer"

    def __str__(self):
        return self.name
