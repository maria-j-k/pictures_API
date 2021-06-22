from django.conf import settings
from django.conf.urls.static import static
from rest_framework import serializers
from easy_thumbnails.files import get_thumbnailer

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
        fields = ('url', )


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
        fields = ('id',  'image', 'owner', 'thumbnails', 'duration')

    def create(self, validated_data):
        request = self.context.get('request')
        picture = Picture.objects.create(**validated_data)
        sizes = picture.owner.plan.thumbsizes.all()
        options = {'crop': True}
        for size in sizes:
            options.update(size.dimensions)
            thumbnailer = get_thumbnailer(picture.image)
            thumb = thumbnailer.get_thumbnail(options)
            url = request.build_absolute_uri(thumb.url)
            t = Thumbnail.objects.create(url=url, picture=picture)
        return picture

