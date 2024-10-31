from enum import Enum
from random import choices

from django.db import models

from base_user.models import BaseUser
from core.models import Vehicle, TimeStampMixin


class DriverType(Enum):
    TRACTOR = 'TRACTOR'

class Driver(TimeStampMixin):
    licence_no = models.CharField(max_length=100, null=False)
    driver_type = models.CharField(
        max_length=20,
        choices=[(tag.name, tag.value) for tag in DriverType]
    )
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)

class DriverVehicleOwner(TimeStampMixin):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

