from datetime import datetime
from django.db.models import fields
from django.utils.timesince import timesince
from django.core.exceptions import ValidationError
from rest_framework import serializers
from news.models import Article, Journalist

class ArticleSerializer(serializers.ModelSerializer):
  """inheriting from the ModelSerializer class has a lot of code with the methods
    so you don't have to write as much"""
  time_since_publication = serializers.SerializerMethodField()
#   author = JournalistSerializer(read_only=True)
  # author = serializers.StringRelatedField()

  class Meta:
      model = Article
      exclude = ("id",)
      # fields = "__all__" # we want all the fields of our model
      # fields = ("title", "description", "body") # we want to choose a couple of fields!

  def get_time_since_publication(self, object):
      publication_date = object.publication_date
      now = datetime.now()
      time_delta = timesince(publication_date, now)
      return time_delta

  def validate(self, data):
      """ check that description and title are different 
      https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
      """
      if data["title"] == data["description"]:
          raise serializers.ValidationError("Title and Description must be different from one another!")
      return data

  def validate_title(self, value):
      """ check that title is at least 30 chars long
      https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
      """
      if len(value) < 30:
          raise serializers.ValidationError("The title has to be at least 30 chars long!")
      return value

class JournalistSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True,
                                                    read_only=True,
                                                    view_name="article-detail"
    )
    # articles = ArticleSerializer(read_only = True, many=True)

    class Meta:
        model = Journalist
        fields = "__all__"

# class ArticleSerializer(serializers.Serializer):
"""Writing a class using the Serializer class doesn't give you many methods and
    you must write many of them but you have more control over the methods"""
#   id = serializers.IntegerField(read_only=True)
#   author = serializers.CharField()
#   title = serializers.CharField()
#   description = serializers.CharField()
#   body = serializers.CharField()
#   location = serializers.CharField()
#   publication_date = serializers.DateField()
#   active = serializers.BooleanField()
#   created_at = serializers.DateTimeField(read_only=True)
#   updated_at = serializers.DateTimeField(read_only=True)

#   def create(self, validated_data):
#     print(validated_data)
#     return Article.objects.create(**validated_data)

#   def update(self, instance, validated_data): 
#     instance.author = validated_data.get('author', instance.author)
#     instance.title = validated_data.get('title', instance.title)
#     instance.description = validated_data.get('description', 
#                                               instance.description)
#     instance.body = validated_data.get('body', instance.body)
#     instance.location = validated_data.get('location', instance.location)
#     instance.publication_date = validated_data.get('publication_date', 
#                                                   instance.publication_date)
#     instance.active = validated_data.get('active', instance.active)
#     instance.save()
#     return instance
  
#   def validate(self, data):
#     """ check that description and title are different """
#     if data["title"] == data["description"]:
#       raise serializers.ValidationError("Title and Description must be different")
#     return data
  
#   def validate_title(self, value):
#     if len(value) < 60:
#       raise serializers.ValidationError("Title must be 60 characters long")
#     return value