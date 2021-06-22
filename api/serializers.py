from rest_framework import serializers
from easy_thumbnails.files import get_thumbnailer

from api.models import Picture, Thumbnail
from users.models import ThumbSize


class PictureCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
            max_length=100, 
            allow_empty_file=False, 
            use_url=False,
            )
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Picture
        fields = ('id',  'image', 'owner', 'duration')


class ThumbSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThumbSize
        fields = ('id', 'name', 'size')


class PictureListSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='short_name')
    sizes = ThumbSizeSerializer(many=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Picture
        fields = ('id',  'image', 'owner', 'duration', 'sizes')


class ThumbnailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Thumbnail
        fields = ('id', 'link_validity', 'url')
        read_only_fields = ('url', )

    def create(self, validated_data):
        request = self.context.get('request')
        link_validity = validated_data.get('link_validity', 3000)
        picture = self.context.get('picture')
        size = self.context.get('size')
        options = {'crop': True}
        options.update(size.dimensions)
        thumbnailer = get_thumbnailer(picture.image)
        thumb = thumbnailer.get_thumbnail(options)
        url = request.build_absolute_uri(thumb.url)
        return Thumbnail.objects.create(
                image=thumb, 
                picture = picture, 
                link_validity=link_validity,
                url = url
                )



