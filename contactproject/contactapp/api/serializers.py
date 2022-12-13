from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from ..models import Profile, Category
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from rest_framework import serializers

from .documents import ProfileDocument

class SearchProfileSerializer(ModelSerializer):
   class Meta:
      model=Profile
      fields= ('id', 'first_name', 'last_name', 'profile_pics',
      'contact_image', 'gender', 'email', 'address', 'category'
      )

class ProfileDocumentSerializer(DocumentSerializer):
   class Meta:
      document= ProfileDocument

      fields= ( 
         'id',
         'first_name',
         'last_name',
         'profile_pics',
         'contact_image',
         'gender',
         'favorites',
         'address'
      )

class ProfileListSerializer(ModelSerializer):
   url= serializers.SerializerMethodField()
   
   class Meta:
      model= Profile
      fields= ['id', 'first_name', 'last_name', 'phone_number', 'url']

   def get_url(self, obj):
         return self.context.get("request").build_absolute_uri("detail/") + str(obj.pk)

class ProfileDetailSerializer(ModelSerializer):
   class Meta:
      model= Profile
      fields='__all__'


class CategorySerializer(ModelSerializer):
   class Meta:
      model= Category
      fields=['name']