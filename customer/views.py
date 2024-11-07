import json
from http import HTTPStatus

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from customer.models import Customer
from customer.seralizer import CustomerCreateSerializer, CustomerSerializer
from utils.cpermission_class import IsCustomer
from utils.response import CResponse


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsCustomer])
def get_my_profile(request):
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        return CResponse(
            http_status_code=HTTPStatus.NOT_FOUND,
            message="Only Customer can access this page"
        )
    except Exception as e:
        print(e)
        return CResponse(
            http_status_code=HTTPStatus.INTERNAL_SERVER_ERROR
        )

    serializer = CustomerSerializer(customer)
    return CResponse(serializer.data)


@api_view(['POST'])
def create_profile(request):
    try:
        data = json.loads(request.body)
        serializer = CustomerCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return CResponse(http_status_code=HTTPStatus.CREATED)
        else:
            return CResponse(http_status_code=HTTPStatus.BAD_REQUEST, data=serializer.errors)
    except Exception as e:
        print(e)
        return CResponse(
            http_status_code=HTTPStatus.INTERNAL_SERVER_ERROR
        )
