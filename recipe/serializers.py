from .models import Comments, Likes
from rest_framework import serializers
from . models import Post, Favorites
from django.db.models import Avg

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
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
        model=Post
        fields='__all__'



    def to_representation(self, instance):
        repr= super().to_representation(instance)
        repr['rating']=instance.reviews.aggregate(Avg('rating'))['rating__avg']
        repr['reviews']=instance.reviews.count()
        repr['likes']=instance.likes.count()
        repr['favorites']=instance.favorites.count()
        return repr


    # def to_representation(self, instance):
    #     repr=super().to_representation(instance)
    #     repr['likes']=instance.likes.count()
    #     return repr



class PostCreateSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # images = RecipeImageSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Post
        fields = ('title', 'body', 'category','images')

    def create(self, validated_data):
        # print('Validated data: ', validated_data)
        request = self.context.get('request')
        # print('FILES', request.FILES)
        created_post=Post.objects.create(**validated_data)
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


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('post',)

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['post'] = PostListSerializer(instance.post).data
        return repr
