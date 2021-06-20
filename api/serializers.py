from rest_framework import serializers
from easy_thumbnails.files import get_thumbnailer

from api.models import Picture, Thumbnail



class DynamicFieldsModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        user = self.context['request'].user
        if not user.plan.original:
            self.fields.pop('image')


class ThumbnailSerializer(serializers.ModelSerializer):
    url = serializers.ImageField(
            max_length=200,
            allow_empty_file=False, 
            use_url=True)

    class Meta:
        model = Thumbnail
        fields = ('url', )


class PictureSerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):
    image = serializers.ImageField(
            max_length=100, 
            allow_empty_file=False, 
            use_url=True,
            )
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    thumbnails = ThumbnailSerializer(
            many=True, 
            read_only=True)

    class Meta:
        model = Picture
        fields = ('id',  'image', 'owner', 'thumbnails')

    def create(self, validated_data):
        picture = Picture.objects.create(**validated_data)
        thumbnailer = get_thumbnailer(picture.image)
        user = validated_data['owner']
        for size in user.plan.thumbsizes.all():
            thumb = thumbnailer.get_thumbnail(size.dimensions)
            t = Thumbnail.objects.create(url=thumb.url, picture=picture)
            picture.thumbnails.add(t)
        picture.save()
        return picture


