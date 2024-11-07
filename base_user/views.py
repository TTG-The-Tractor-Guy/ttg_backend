import json
from http import HTTPStatus

from django.shortcuts import render
from rest_framework.decorators import api_view

from utils.response import CResponse


# Create your views here.

@api_view(['POST'])
def sign_up(request):
    try:
        data = json.loads(request.body)
    except Exception as e:
        print(e)
        return CResponse(
            http_status_code=HTTPStatus.INTERNAL_SERVER_ERROR
        )