from rest_framework import serializers
from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.templatetags.thumbnail import thumbnail_url

from api.models import Picture, Thumbnail



class DynamicFieldsModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        user = self.context['request'].user
        if user.plan.original:
            setattr(self.fields['image'], 'use_url', True)


class ThumbnailSerializer(serializers.ModelSerializer):
    url = serializers.URLField()

    class Meta:
        model = Thumbnail
        fields = ('url', 't_url')


class PictureSerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):
    image = serializers.ImageField(
            max_length=100, 
            allow_empty_file=False, 
            use_url=False,
            )
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    thumbnails = ThumbnailSerializer(
            many=True, 
            read_only=True)

    class Meta:
        model = Picture
        fields = ('id',  'image', 'owner', 'thumbnails', 'expires')

    def create(self, validated_data):
        picture = Picture.objects.create(**validated_data)
        user = validated_data['owner']
        sizes = validated_data['owner'].plan.thumbsizes.all()
        for size in sizes:
            url = thumbnail_url(picture.image, size.name)
            thumbnailer = get_thumbnailer(picture.image)
            thumb = thumbnailer.get_thumbnail(size.dimensions)
            t_url = thumb.url
            t = Thumbnail.objects.create(url=url, t_url=t_url, picture=picture)
            picture.thumbnails.add(t)
        picture.save()
        return picture


