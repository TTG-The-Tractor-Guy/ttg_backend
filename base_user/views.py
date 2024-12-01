import json
import traceback
from http import HTTPStatus

from rest_framework.decorators import api_view

from base_user.serializer import BaseUserSerializer
from utils.response import CResponse

@api_view(['POST'])
def sign_up(request):
    try:
        data = json.loads(request.body)
        serializer = BaseUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return CResponse(
                http_status_code=HTTPStatus.CREATED,
                message="User Created Successfully",
                data=serializer.data
            )
        else:
            print(serializer.errors)
            return CResponse(
                http_status_code=HTTPStatus.BAD_REQUEST,
                data=serializer.errors
            )
    except Exception as e:
        traceback.print_exc()
        return CResponse(
            http_status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            message=str(e)
        )