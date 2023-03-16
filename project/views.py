from django.forms.models import model_to_dict
from .models import ProductModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer


@api_view(http_method_names=["GET"])
def welcome(request):
    instance = ProductModel.objects.get(id=2)
    if instance:
        data = ProductSerializer(instance=instance).data
    print(data)
    return Response(data)

@api_view(http_method_names=["GET"])
def get_request(request):
    return Response(request)

@api_view(["POST"])
def validate_data(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.data
        return Response(data)
