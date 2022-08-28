from .models import Comments, Likes
from rest_framework import serializers
from . models import Recipe
from django.db.models import Avg

class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=('title', 'image')

    # def to_representation(self, instance):
    #     repr= super().to_representation(instance)
    #     repr['rating']=instance.reviews.aggregate(Avg('rating'))['rating__avg']
    
class CommentSerilizer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.email')
    class Meta:
        model=Comments
        fields=('user', 'body','post')

class RecipeDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerilizer(many=True, read_only=True)
    
    class Meta:
        model=Recipe
        fields='__all__'



    def to_representation(self, instance):
        repr= super().to_representation(instance)
        repr['rating']=instance.reviews.aggregate(Avg('rating'))['rating__avg']
        repr['reviews']=instance.reviews.count()
        return repr


    def to_representation(self, instance):
        repr=super().to_representation(instance)
        repr['likes']=instance.likes.count()
        return repr



class PostCreateSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # images = RecipeImageSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Recipe
        fields = ('title', 'body', 'category', 'preview', 'images')

    def create(self, validated_data):
        # print('Validated data: ', validated_data)
        request = self.context.get('request')
        # print('FILES', request.FILES)
        created_post=Recipe.objects.create(**validated_data)
        images_data=request.FILES
        # print(created_post)
        # print('work',images_data.getlist('images'))
        # images_object=[PostImages(post=created_post,image=image) for image in images_data.getlist('images')]
        # PostImages.objects.bulk_create(images_object)
        return created_post

class LikeSerializer(serializers.ModelSerializer):
    # user=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Likes
        fields=('user',)
