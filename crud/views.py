from rest_framework import generics, mixins, permissions, authentication
from .permissions import IsStaffEditorPermission
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import ProductModel
from . import authentication as auth

from rest_framework.status import (
    HTTP_204_NO_CONTENT,
    HTTP_201_CREATED,
    HTTP_200_OK, 
)
import io
import datetime

# io.BytesIO()

# class based views #########################################################################
class RetrieveProductView(generics.RetrieveAPIView):
    """Retrieving data READ Method"""

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission]
    serializer_class = ProductSerializer
    queryset = ProductModel



class CreateProducView(generics.CreateAPIView):
    """Creating data in model. CREATE Method"""
    queryset = ProductModel
    serializer_class = ProductSerializer

    def perfom_create(self, serializer):
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            content = serializer.validated_data["content"]
            price = serializer.validated_data["price"]
            self.queryset(name=name, content=content, price=price).save()
            return Response(data={"status": "Success!", "msg": "Data created successfully!"}, status=HTTP_201_CREATED)
        else:
            return Response({"status": "Failed!", "msg": "Validation failed"})

class ProductUpdateView(generics.UpdateAPIView):
    """Update view with class based view. UPDATE Method"""
    queryset = ProductModel
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        serializer.save()


class ProductDeleteView(generics.DestroyAPIView):
    """Delete view in class based view. DELETE Method"""
    queryset = ProductModel
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        query = self.queryset.objects.filter()

# function based view #######################################################################
@api_view(http_method_names=["GET", "POST"])
def retrieve_and_create(request, pk=None, *args, **kwargs):
    """Create and retrieve view in function based view"""
    if request.method == "GET":
        if pk is not None:
            queryset = get_object_or_404(ProductModel, id=pk)
            return Response(queryset)
        objects = ProductModel.objects.all()
        serializer = ProductSerializer(instance=objects, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            content = serializer.validated_data["content"]
            price = serializer.validated_data["price"]
            model = ProductModel(name=name, content=content, price=price)
            model.save()
            return Response({"Success": "Data saved successfully!"})

# Delete and Edit at once
@api_view(http_method_names=["PUT"])
def update(request, pk, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        content = serializer.validated_data["content"]
        price = serializer.validated_data["price"]
        name = serializer.validated_data["name"]
        instance = ProductModel.objects.get(id=pk)
        instance.content = content
        instance.price = price
        instance.name = name
        instance.save()
    return Response({"msg": "Data updated successfully!"})

@api_view(http_method_names=["DELETE"])
def delete(request, pk, *args, **kwargs):
    instance = ProductModel.objects.get(id=pk)
    instance.delete()
    instance.save()

# Generics and Mixins #######################################################################
class ProductRetrieveModelMixinView(generics.RetrieveAPIView, mixins.RetrieveModelMixin):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission]
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get_queryset(self) -> dict:
        print(self.kwargs["pk"])
        if self.lookup_field is None:
            return self.queryset
        data_to_be_fetched = self.queryset.filter(id=self.kwargs["pk"]).values()
        return data_to_be_fetched

    def get(self, request, *args, **kwargs):
        context = self.get_queryset()
        if not context:
            return Response(data={"status": "Fail", "msg": f"Data with id: {self.kwargs['pk']} not found"})
        return Response(data=context, status=HTTP_200_OK)

class ProductListModelMixinView(generics.ListAPIView, mixins.ListModelMixin):
    authentication_classes = [
        authentication.SessionAuthentication, 
        auth.BearerTokenAuthentication
    ]
    permission_classes = [IsStaffEditorPermission]
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

    def __repr__(self):
        return """Product Model for retrieving list of all data in the database"""

    def get(self, request, *args, **kwargs):
        return self.list(request=request, args=args, kwargs=kwargs)

class ProductCreateModelMixinView(generics.CreateAPIView, mixins.CreateModelMixin):
    serializer_class = ProductSerializer
    
    def post(self, request, *args, **kwargs):
        if self.serializer_class(data=request.data).is_valid():
            request.data["content"] = request.data.get("name") 
        context = {
            "is_success": True,
            "msg": "Data created and saved successfully!",
            "time": str(datetime.datetime.now())
        }
        self.create(request=request, args=args, kwargs=kwargs)
        return Response(data=context, status=HTTP_201_CREATED)

class ProductUpdateModelMixinView(generics.UpdateAPIView, mixins.UpdateModelMixin):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def put(self, request, *args, **kwargs):
        context = {
            "is_success": True,
            "msg": "Data updated successfully!",
            "time": str(datetime.datetime.now())
        }
        self.update(request=request, args=args, kwargs=kwargs)
        return Response(data=context, status=HTTP_200_OK)
    
class ProductDeleteModelMixin(generics.DestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get_queryset(self):
        if self.queryset is None:
            return self.queryset
        data = self.queryset.filter(id=self.kwargs["pk"])
        return data

    def delete(self, request, *args, **kwargs):
        if len(self.get_queryset()) == 0:
            return Response(data={"status": "Fail", "msg": f"Data with id: {self.kwargs['pk']} not found"})
        self.get_queryset().delete()
        return Response(status=HTTP_204_NO_CONTENT)

class ProductDeleteAllModelMixinView(generics.DestroyAPIView):
    """
    Not so understandable what I am doing but surely know, that as I practice more
    I will realize the need of those things -> generic views, api views, function based
    views, class based views.
    """
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ["delete"]

    def destroy(self, request, *args, **kwargs):
        self.get_queryset().delete()
        return Response(status=204)
 
# https://www.canva.com/design/DAFYMEpLnv4/BvPurNW-2XtgtS_ulsGzEg/edit

# NOTE: For authentication order, or in order to securely transport data through clients the best tool to use 
# is JWT which should be pip installed like """python-jose"""
