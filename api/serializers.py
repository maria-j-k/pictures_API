from rest_framework import serializers
from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.templatetags.thumbnail import thumbnail_url

from api.models import Picture, Thumbnail



class DynamicFieldsModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        user = self.context['request'].user
        if user.plan.original:
            setattr(self.fields['image'], 'use_url', True)


class ThumbnailSerializer(serializers.ModelSerializer):
#    url = serializers.URLField()
    image = serializers.ImageField(
            max_length=200,
            allow_empty_file=False, 
            use_url=True,
            )

    class Meta:
        model = Thumbnail
#        fields = ('url', 't_url')
        fields = ('image', )

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
        thumbnailer = get_thumbnailer(picture.image)
        user = validated_data['owner']
        sizes = validated_data['owner'].plan.thumbsizes.all()
        for size in sizes:
            url = thumbnail_url(picture.image, size.name)
            thumb = thumbnailer.get_thumbnail(size.dimensions)
            t_url = thumb.url
            t = Thumbnail.objects.create(image=thumb, picture=picture)
            picture.thumbnails.add(t)
        picture.save()
        return picture


