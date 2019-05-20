from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as st

from .models import News
from .serializers import NewsListSerializers, NewsDetailSerializers


class NewsListAPIView(APIView):
    def get(self, request) -> Response:
        queryset = News.objects.all()
        serializers = NewsListSerializers(queryset, many=True)
        return Response({'result': serializers.data}, status=st.HTTP_200_OK)


class NewsDetailAPIView(APIView):
    def get(self, request, pk) -> Response:
        queryset = News.objects.get(pk=pk)
        serializers = NewsDetailSerializers(queryset)
        return Response({'result': serializers.data}, status=st.HTTP_200_OK)
