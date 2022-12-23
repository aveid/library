from rest_framework import serializers

# class BookSerializers(serializers.Serializer):
#     title = serializers.CharField()
#     desc = serializers.CharField()
#     author = serializers.CharField()
#     year = serializers.IntegerField()
from book.models import Book, Picture

class PictureSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = "__all__"


class BookSerializers(serializers.ModelSerializer):
    # genre = serializers.CharField(source='genre.title', read_only=True)

    class Meta:
        model = Book
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.genre:
            representation['genre'] = instance.genre.title
        if instance.pictures.exists():
            representation['pictures'] = PictureSerizlizer(instance.pictures.all(),
                                                           many=True).data

        return representation