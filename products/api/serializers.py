from products.models import Category, Tag, Recipe, Subscriber
from rest_framework import serializers


class SubscriberCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = (
            'email',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title'
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'title'
        )


class RecipeSerializer(serializers.ModelSerializer):

    # category = serializers.CharField(source = 'category.title')
    category = CategorySerializer()
    tags = TagSerializer(many = True)


    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'category',
            'tags',
            'author_name',
            'small_description',
            'description',
            'slug',
            'image',
            'cover_image'
        )


class RecipeCreateSerializer(serializers.ModelSerializer):

    author = serializers.PrimaryKeyRelatedField(read_only = True)

    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'category',
            'tags',
            'author',
            'small_description',
            'description',
            'slug',
            'image',
            'cover_image'
        )

    def validate(self, attrs):
        request = self.context['request']
        attrs['author'] = request.user
        return super().validate(attrs)