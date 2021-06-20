from rest_framework import serializers

from api.models import Picture


class PictureSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
            max_length=100, 
            allow_empty_file=False, 
            use_url=True,
            )
    owner = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
            )
    class Meta:
        model = Picture
        fields = ('id',  'image', 'owner')

    def create(self, validated_data):
        return Picture.objects.create(**validated_data)
