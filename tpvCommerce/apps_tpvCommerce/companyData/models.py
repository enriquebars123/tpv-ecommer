from django.db import models


class country(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        db_table = "country"

    def __str__(self):
        return self.name


class township(models.Model):
    name = models.CharField(max_length=250)
    zone = models.ForeignKey(country, on_delete=models.CASCADE)

    class Meta:
        db_table = "township"

    def __str__(self):
        return self.name


class dealer(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    rut = models.CharField(max_length=80)
    phone = models.CharField(max_length=30)
    web = models.CharField(max_length=255)
    city = models.ForeignKey(township, on_delete=models.CASCADE)

    class Meta:
        db_table = "dealer"

    def __str__(self):
        return self.name
