from rest_framework import serializers
from .models import News, Image


class NewsImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model: object = Image
        fields: tuple = ('image', 'alt')


class NewsDetailSerializers(serializers.ModelSerializer):
    images = NewsImagesSerializers(many=True)
    date = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model: object = News
        fields: tuple = ('id', 'title', 'short_description', 'description', 'preview_image', 'date', 'images')


class NewsListSerializers(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model: object = News
        fields: tuple = ('id', 'title', 'short_description', 'preview_image', 'date')
