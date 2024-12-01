import json
import traceback
from http import HTTPStatus
from turtledemo.clock import datum

from django.template.context_processors import media
from pyexpat.errors import messages
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from utils.cpermission_class import IsDriver, IsCustomer, IsLoggedIn
from utils.response import CResponse


@api_view(['GET'])
@permission_classes([IsLoggedIn])
def test_view(request):
    return Response(
        data={"Hello":"World"}
    )


@api_view(['GET'])
@permission_classes([IsLoggedIn])
def self_register(request):
    try:
        if request.body:
            data = json.loads(request.body)
        else:
            return CResponse(http_status_code=HTTPStatus.BAD_REQUEST)
        return CResponse(
            data=data,
            http_status_code=HTTPStatus.CREATED,
            message="Customer Account Created"
        )
    except Exception as e:
        traceback.print_exc()
        return CResponse(
            message=str(e)
        )