from rest_framework import serializers
from .models import Category


#http://stackoverflow.com/questions/13376894/django-rest-framework-nested-self-referential-objects

class RecursiveField(serializers.Serializer):
    def to_native(self, value):
        return self.parent.to_native(value)


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class CategorySerializer(serializers.ModelSerializer):
    #parent = serializers.HyperlinkedRelatedField(view_name='categories-detail')
    #   parent = SubCategorySerializer()
    #subcategories = SubCategorySerializer(read_only=True)
    subcategories = RecursiveField(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'subcategories')


class CategorySerializer2(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Category
        fields = ('id', 'parent', 'name', 'subcategories')

CategorySerializer.base_fields['subcategories'] = CategorySerializer2()
