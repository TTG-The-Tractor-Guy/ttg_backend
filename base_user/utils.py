from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy


@deconstructible
class IndianMobileNumberValidator(validators.RegexValidator):
    regex = r"^(?:\+91|91)?[789]\d{9}$"
    message = gettext_lazy("Enter a valid Indian mobile number. It must start with 7, 8, or 9 and be 10 digits long.")
    flags = 0