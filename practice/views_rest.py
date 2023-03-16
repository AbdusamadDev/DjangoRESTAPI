from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponseBadRequest
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from practice import serializers, models
from rest_framework import generics
from rest_framework.status import *
from practice.models import Snippet


class FetchDataView(generics.RetrieveAPIView, generics.DestroyAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.Snippet.objects.all()
    lookup_field = "pk"
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.queryset
        content = self.queryset.get(pk=pk)
        return content

    def delete(self, request, pk=None, *args, **kwargs):
        if pk is None:
            raise HttpResponseBadRequest(content={"msg": "Bad request: provide pk"})
        self.get_queryset().delete()
        return Response(status=HTTP_204_NO_CONTENT)

    # def retrieve(self, request, pk=None, *args, **kwargs):
    #     if pk is None:
    #         return Response({"msg": "please provide pk"})
    #     serializer = serializers.SnippetSerializer(data=self.get_queryset(pk=pk))
    #     serializer.is_valid(raise_exception=True)
    #     return serializer.data
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = serializer.SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializer.SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
