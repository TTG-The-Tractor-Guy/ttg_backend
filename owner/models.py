from django.db import models

from base_user.models import BaseUser
from core.models import Vehicle, TimeStampMixin


class Owner(TimeStampMixin):
    company_name = models.CharField(max_length=512, null=True)
    extra_information = models.JSONField()



class OwnerUsers(TimeStampMixin):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)


class OwnerVehicle(TimeStampMixin):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
