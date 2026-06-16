from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    purchase_date = models.DateField()
    department = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name