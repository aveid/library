from rest_framework import serializers

class BookSerializers(serializers.Serializer):
    title = serializers.CharField()
    desc = serializers.CharField()
    author = serializers.CharField()
    year = serializers.IntegerField()
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


class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        extra_kwargs = {"author": {"required": False},
                        "year": {"required": False},
                        "title": {"required": False},
                        "desc": {"required": False},
                        }

    def update(self, instance, validated_data):
        instance.year = validated_data.get("year", instance.year)
        instance.title = validated_data.get("title", instance.title)
        instance.desc = validated_data.get("desc", instance.desc)
        instance.author = validated_data.get("author", instance.author)
        instance.save()
        return instance



