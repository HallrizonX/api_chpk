from django.conf import settings
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status as st
from utils import bad_request


class ReadOnlyModelMixinViewSet(ReadOnlyModelViewSet):
    model = None
    queryset = None
    serializer_class = None

    @bad_request
    @method_decorator(cache_page(settings.CACHE_TTL))
    def list(self, request, *args, **kwargs) -> Response:
        assert self.queryset is not None, "Queryset is require"
        assert self.serializer_class is not None, "Serializer class is require"

        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)

    @bad_request
    @method_decorator(cache_page(settings.CACHE_TTL))
    def retrieve(self, request, *args, **kwargs) -> Response:
        assert self.queryset is not None, "Queryset is require"
        assert self.serializer_class is not None, "Serializer class is require"
        assert self.model is not None, "Model is required"

        queryset = self.model.objects.get(pk=kwargs.get('pk'))
        serializer = self.serializer_class(queryset)
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)
