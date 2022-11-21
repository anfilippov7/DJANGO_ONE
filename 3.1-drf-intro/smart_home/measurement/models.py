from django.db import models


class Sensor(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    date_measurement = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='image')
