from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status as st
from rest_framework import permissions

from .models import Profile
from .serializers import ProfileSerializers


class ProfileViewSet(ReadOnlyModelViewSet):
    permission_classes = (permissions.AllowAny,)  # Test permission

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers

    def list(self, request, *args, **kwargs):
        serializer = ProfileSerializers(self.get_queryset(), many=True)
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        queryset = Profile.objects.get(pk=kwargs.get('pk'))
        serializer = ProfileSerializers(queryset)
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)

