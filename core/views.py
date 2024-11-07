from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from utils.cpermission_class import IsDriver, IsCustomer
from utils.response import CResponse


# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsDriver, IsCustomer])
def test_view(request):
    return Response(
        data={"Hello":"World"}
    )

@api_view(['POST'])
def sign_up():
    return CResponse(
        data={
            "New Data"
        }
    )