from rest_framework import serializers
from easy_thumbnails.templatetags.thumbnail import thumbnail_url

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
        fields = ('id',  'image', 'owner')


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
        fields = ('id',  'image', 'owner', 'sizes')


class ThumbnailSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Thumbnail
        fields = ('id', 'link_validity', 'url')

    def create(self, validated_data):
        link_validity = validated_data.get('link_validity', 300)
        picture = self.context.get('picture')
        size = self.context.get('size')
        return Thumbnail.objects.create(
                picture = picture, 
                link_validity=link_validity,
                size = size,
                )
    
    def get_url(self, obj):
        request = self.context.get('request')
        alias = self.context['size'].name
        url = thumbnail_url(obj.image, alias)
        return  request.build_absolute_uri(url)


