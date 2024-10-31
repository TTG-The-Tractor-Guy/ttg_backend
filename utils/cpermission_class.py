from rest_framework.permissions import BasePermission

from customer.models import PermittedUser, Customer
from driver.models import Driver
from owner.models import OwnerUsers


class IsDriver(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        if request.user.is_staff:
           return True

        # Check if a Driver instance exists for this user
        return Driver.objects.filter(user=request.user).exists()


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        if request.user.is_staff:
           return True

        # Check if a Driver instance exists for this user
        return OwnerUsers.objects.filter(user=request.user).exists()

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        if request.user.is_staff:
           return True


        # Check if a Driver instance exists for this user
        return (
                PermittedUser.objects.filter(customer__user=request.user).exists() or
                Customer.objects.filter(user=request.user).exists()
        )
