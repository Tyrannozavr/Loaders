from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Loader(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    number = models.CharField(max_length=120, unique=True)
    capacity = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Грузоподъемность")
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.number


class Incidents(models.Model):
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    loader = models.ForeignKey(Loader, on_delete=models.SET_NULL, null=True, blank=True)
