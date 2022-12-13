from contactapp.models import Profile, Category
from .documents import ProfileDocument
from rest_framework import generics
from .paginations import ResponsePagination
from contactapp.api.serializers import ProfileListSerializer, ProfileDetailSerializer, CategorySerializer, ProfileDocumentSerializer
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet, BaseDocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import CompoundSearchFilterBackend, SuggesterFilterBackend
from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION



class ProfileDocumentView(DocumentViewSet):
   document= ProfileDocument
   serializer_class= ProfileDocumentSerializer

   filter_backends = [CompoundSearchFilterBackend]
   search_fields= ('id', 'first_name', 'last_name', 'profile_pics',
      'contact_image', 'gender', 'email', 'address', 'category.name'
      )

   suggester_fields = {
      'first_name': {
         'field': 'first_name.suggest',
         'suggesters': [
            SUGGESTER_COMPLETION,
            ],
      },
      'last_name':{
         'field': 'last_name.suggest',
         'suggesters': [ 
            SUGGESTER_COMPLETION,
         ],
      },
      'category':{
         'field': 'category.suggest',
         'suggesters': [ 
            SUGGESTER_COMPLETION,
         ],
      }
   }
   ordering= ('-created_at')


class ProfileListCreate(generics.ListCreateAPIView):
   serializer_class = ProfileListSerializer
   queryset= Profile.objects.all()
   pagination_class = ResponsePagination

class ProfileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = ProfileDetailSerializer
   queryset= Profile.objects.all()


class CategoryList(generics.ListCreateAPIView):
   serializer_class = CategorySerializer
   queryset= Category.objects.all()


