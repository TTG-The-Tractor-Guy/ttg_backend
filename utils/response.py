from enum import Enum
from http import HTTPStatus
from rest_framework.response import Response

class CResponse(Response):
    def __init__(self, http_status_code: HTTPStatus, message: str = None, data=None):
        response_json = {}

        match http_status_code:
            case HTTPStatus.OK:  # 200
                response_json['message'] = message
                response_json['success'] = True
                if data:
                    response_json['data'] = data

            case HTTPStatus.CREATED:  # 201
                response_json['message'] = message
                response_json['success'] = True
                if data:
                    response_json['data'] = data

            case HTTPStatus.BAD_REQUEST:  # 400
                response_json['message'] = message or "Bad Request"
                response_json['success'] = False
                if data:
                    response_json['errors'] = data  # Assume data contains error details

            case HTTPStatus.NOT_FOUND:  # 404
                response_json['message'] = message or "Not Found"
                response_json['success'] = False

            case HTTPStatus.INTERNAL_SERVER_ERROR:  # 500
                response_json['message'] = message or "Internal Server Error, Please contact admin"
                response_json['success'] = False

            case _:
                response_json['message'] = message or "An unexpected error occurred"
                response_json['success'] = False

        super().__init__(data=response_json, status=http_status_code)
