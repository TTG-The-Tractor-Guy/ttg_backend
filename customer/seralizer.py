from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from base_user.models import BaseUser
from customer.models import Customer


class CustomerCreateSerializer(serializers.ModelSerializer):
    care_of = serializers.CharField(required=False)

    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        # Extract user-related data
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        mobile = validated_data.pop('mobile')
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        try:
            # Validate and create the BaseUser using BaseUserSerializer
            user = BaseUser(
                first_name=first_name,
                last_name=last_name,
                mobile=mobile,
                email=email
            )
            user.set_password(password)  # Ensure the password is hashed
            user.save()

            # Create the Customer instance linked to the user
            customer = Customer.objects.create(user=user, care_of=validated_data.get('care_of'))

            return customer

        except Exception as e:
            raise ValidationError({"error": "User creation failed", "details": str(e)})



class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ['id', 'care_of', 'user']

    def get_user(self, obj):
        return {
            "first_name": obj.user.first_name,
            "last_name": obj.user.last_name,
            "mobile": obj.user.mobile,
            "email": obj.user.email,
        }

class CustomerUpdateSerializer(serializers.ModelSerializer):
    care_of = serializers.CharField(required=False)

    class Meta:
        model = Customer
        fields = ['care_of']

    def update(self, instance, validated_data):
        instance.care_of = validated_data.get('care_of', instance.care_of)
        instance.save()
        return instance