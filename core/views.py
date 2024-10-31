from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from utils.cpermission_class import IsDriver, IsCustomer


# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsDriver, IsCustomer])
def test_view(request):
    return Response(
        data={"Hello":"World"}
    )