from django.db import models

from base_user.models import BaseUser
from core.models import TimeStampMixin


# Create your models here.


class Customer(TimeStampMixin):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    care_of = models.CharField(max_length=255, verbose_name='C/O', default=None, null=True)

class PermittedUser(TimeStampMixin):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    permitted_user = models.ForeignKey(BaseUser, on_delete=models.DO_NOTHING, null=True, default=None)
    is_existing_user = models.BooleanField(default=False)
    permitted_till = models.DateTimeField(default=None, null=True)






