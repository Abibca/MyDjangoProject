from rest_framework.response import Response
from .models import Userprofile,Address_details
from .serializer import Userprofileserializer,Address_detailsserializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_profile(request):
    user_info= Userprofile.objects.all()
    example = Userprofileserializer(user_info, many=True)   
    return Response(example.data,status=200)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_address(request):
    user_info= Address_details.objects.all()
    example = Address_detailsserializer(user_info, many=True)   
    return Response(example.data,status=200)


# Create your views here.
