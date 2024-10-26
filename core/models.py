from django.db import models

class TimeStampMixin(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Vehicle(TimeStampMixin):
    vehicle_no = models.CharField(max_length=20, null=False, unique=True)
    vehicle_details = models.JSONField(null=True)